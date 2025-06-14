---

# 🛣️ Road Lane Line Detection System

A real-time lane detection system that processes road videos or live webcam feeds to identify and mark road lanes. Built using OpenCV, NumPy, and Python, this project aims to improve road safety by providing accurate lane detection and real-time voice alerts when lane markers are not visible.

---

## 📌 Project Overview

This system detects lane lines from dashcam videos or a live camera feed, highlights them using Hough Transform, and gives audio feedback to the driver when lanes are not detected. It uses basic computer vision techniques and provides a Tkinter-based GUI for selecting video files or webcam feed.

---

## ✨ Features

* 🎥 **Supports Any Road Video or Live Webcam Feed**
* 🧠 **Canny Edge Detection + Hough Line Transform**
* 🟨 **Region of Interest Selection for Focusing on Roads**
* 📢 **Voice Feedback if Lanes are Missing**
* 🖥️ **Attractive and Centered Tkinter GUI**
* 💡 **Handles Grayscale or Color Frame Inputs**
* ⚙️ **Efficient and Fast Frame Processing in Real-Time**

---

## 🛠️ Technologies Used

* Python 3.12+
* OpenCV
* NumPy
* Tkinter
* pyttsx3 (Text-to-Speech for voice alerts)
* MoviePy (for video handling)

---

## 🚀 How to Run

### 1. Install Dependencies

```bash
pip install opencv-python numpy pyttsx3 moviepy
```

### 2. Run the Project

```bash
python task-1.py
```

---

## 🧪 Modes of Operation

* **📁 Video Input Mode**: Upload any road video and get processed output with lane lines.
* **📷 Live Webcam Mode**: Detect lane lines live using your computer's camera.

---

## 📢 Voice Feedback

If one or both lanes are not detected, the system will automatically announce:

```
"Warning: One or both lanes not detected. Ensure camera is positioned correctly."
```

This ensures added safety for real-time use.

---

## 🖼️ Sample Output

> Detected lanes will be highlighted in yellow lines drawn over the road footage.

---

## 📂 Folder Structure

```
📁 roadlanelinedetectionsystem/
│
├── task-1.py               # Main Python script
├── test_videos/            # Optional test video folder
├── README.md               # This file
```

---

## 🎓 Internship Context

This project was developed as **Task 1** under the **Next24tech AICTE Internship Program**. It demonstrates real-time computer vision application using traditional AI techniques to improve driver assistance systems.

---

## 📧 Contact

**Sampathirao Kavya**
Email: [kavs14345@gmail.com](mailto:kavs14345@gmail.com)
Program: B.Tech CSE, JNTU-GV
Internship ID: NIP/2025/05A001
Mentor: Next24tech Technologies Pvt. Ltd.

---
