import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import threading
import pyttsx3

engine=pyttsx3.init()
engine.setProperty('rate',160)

def speak(text):
    threading.Thread(target=lambda: engine.say(text) or engine.runAndWait()).start()
    
def region_selection(image):
    mask=np.zeros_like(image)
    if len(image.shape)==3:
        ignore_mask_color=(255,)*image.shape[2]
    else:
        ignore_mask_color=255
    rows,cols=image.shape[:2]
    bottom_left=[cols*0.1,rows*0.95]
    top_left=[cols*0.4,rows*0.6]
    bottom_right=[cols*0.9,rows*0.95]
    top_right=[cols*0.6,rows*0.6]
    vertices=np.array([[bottom_left,top_left,top_right,bottom_right]],dtype=np.int32)
    cv2.fillPoly(mask,vertices,ignore_mask_color)
    return cv2.bitwise_and(image,mask)

def draw_lines(img,lines):
    line_img=np.zeros_like(img)
    if lines is None:
        return img
    for line in lines:
        if line is not None:
            x1,y1,x2,y2=line
            cv2.line(line_img,(x1,y1),(x2,y2),(255,0,0),5)
    return cv2.addWeighted(img,0.8,line_img,1.0,0.0)

def average_slope_intercept(lines):
    left_lines,right_lines=[],[]
    for line in lines:
        for x1,y1,x2,y2 in line:
            if x2==x1:
                continue
            slope=(y2-y1)/(x2-x1)
            intercept=y1-slope*x1
            if slope<-0.3:
                left_lines.append((slope,intercept))
            elif slope>0.3:
                right_lines.append((slope,intercept))
    left=np.mean(left_lines,axis=0) if left_lines else None
    right=np.mean(right_lines,axis=0) if right_lines else None
    return left, right

def pixel_points(y1,y2,line):
    if line is None:
        return None
    slope,intercept=line
    try:
        x1=int((y1-intercept)/slope)
        x2=int((y2-intercept)/slope)
        return [x1,y1,x2,y2]
    except:
        return None

def detect_lanes(image):
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    blur=cv2.GaussianBlur(gray,(5,5),0)
    edges=cv2.Canny(blur,50,150)
    roi=region_selection(edges)
    lines=cv2.HoughLinesP(roi,1,np.pi/180,threshold=40,minLineLength=50,maxLineGap=100)
    if lines is not None:
        left,right=average_slope_intercept(lines)
        y1=image.shape[0]
        y2=int(y1*0.6)
        left_line=pixel_points(y1,y2,left)
        right_line=pixel_points(y1,y2,right)
        if left_line is None or right_line is None:
            speak("Warning: One or both lanes not detected.")
        return draw_lines(image,[left_line,right_line])
    else:
        speak("No lanes detected.")
        return image

class LaneDetectionApp:
    def __init__(self,root):
        self.root=root
        self.root.title("🚘 Lane Detection System")
        self.root.geometry("1200x700")
        self.root.configure(bg="lightblue")

        self.video_source=None
        self.use_webcam=False
        self.running=False

        tk.Label(root,text="Input Video",font=("Arial",14),bg="lightblue").place(x=150,y=20)
        tk.Label(root,text="Detected Output",font=("Arial",14),bg="lightblue").place(x=800,y=20)

        self.input_label=tk.Label(root,bg="black")
        self.input_label.place(x=50,y=60,width=500,height=400)

        self.output_label=tk.Label(root,bg="black")
        self.output_label.place(x=650,y=60,width=500,height=400)

        tk.Button(root,text="📂 Upload Video",font=("Arial",12),command=self.load_video,bg="#4CAF50",fg="white").place(x=150,y=500)
        tk.Button(root,text="🎥 Use Webcam",font=("Arial",12),command=self.use_webcam_video,bg="#9C27B0",fg="white").place(x=350,y=500)
        tk.Button(root,text="▶ Start Detection",font=("Arial",12),command=self.start_detection,bg="#2196F3",fg="white").place(x=550,y=500)
        tk.Button(root,text="⛔ Stop",font=("Arial",12),command=self.stop_detection, bg="#f44336",fg="white").place(x=750,y=500)

    def load_video(self):
        self.video_source=filedialog.askopenfilename(title="Select Video File",filetypes=[("MP4 files","*.mp4"), ("All files","*.*")])
        self.use_webcam=False
        speak("Video file selected.")

    def use_webcam_video(self):
        self.video_source=0
        self.use_webcam=True
        speak("Webcam selected.")

    def start_detection(self):
        if self.video_source is None:
            speak("Please upload a video or select webcam.")
            return
        self.running=True
        threading.Thread(target=self.process_video).start()

    def stop_detection(self):
        self.running=False
        speak("Detection stopped.")

    def process_video(self):
        cap=cv2.VideoCapture(self.video_source)
        while cap.isOpened() and self.running:
            ret,frame=cap.read()
            if not ret:
                break
            processed=detect_lanes(frame.copy())

            input_img=cv2.resize(frame,(500,400))
            output_img=cv2.resize(processed,(500,400))
            input_img=cv2.cvtColor(input_img,cv2.COLOR_BGR2RGB)
            output_img=cv2.cvtColor(output_img,cv2.COLOR_BGR2RGB)

            input_photo=ImageTk.PhotoImage(Image.fromarray(input_img))
            output_photo=ImageTk.PhotoImage(Image.fromarray(output_img))

            self.input_label.config(image=input_photo)
            self.output_label.config(image=output_photo)

            self.input_label.image=input_photo
            self.output_label.image=output_photo
        cap.release()

if __name__=="__main__":
    root=tk.Tk()
    app=LaneDetectionApp(root)
    root.mainloop()