
# 🎓 Next24tech AICTE Internship – AI/ML Development (June–July2025)

Welcome to the official project documentation of the **Next24tech AICTE Internship Program**. This internship focused on real-world AI/ML applications through a hands-on, task-based structure. Over the course of the internship, I successfully completed **three comprehensive AI/ML projects**, each addressing a unique societal or technical challenge using machine learning, deep learning, or computer vision techniques.

---

## 🗂️ Table of Contents

* [Internship Overview](#-internship-overview)
* [Task 1: Road Lane Line Detection System](#1-road-lane-line-detection-system)
* [Task 2: Plant Leaf Disease Detection System](#2-plant-leaf-disease-detection-system)
* [Task 3: Summer Heatwaves Mobile Alert System](#3-summer-heatwaves-mobile-alert-system)
* [Tech Stack Used](#-tech-stack-used)
* [Installation Guide](#-installation-guide)
* [Results & Demos](#-results--demos)
* [Conclusion](#-conclusion)
* [Contact](#-contact)

---

## 📚 Internship Overview

The **Next24tech AICTE Internship Program** provided a structured, challenge-driven experience that enhanced my technical skills in AI/ML development. The internship was divided into **three tasks**, each requiring problem analysis, data preparation, model training, implementation, and deployment through desktop or mobile interfaces. I gained practical experience in **computer vision**, **deep learning**, and **AI-powered alert systems**—bridging academic knowledge with real-world applications.

---

## ✅ 1. Road Lane Line Detection System

### 📌 Objective:

To develop a real-time system that detects road lane lines from dashcam videos or live webcam feeds using computer vision techniques. It enhances road safety and awareness for autonomous driving or driver assistance systems.

### 🔍 Key Features:

* Processes uploaded road videos or webcam feeds
* Detects left and right lane markers using **Canny Edge Detection** and **Hough Line Transform**
* Highlights lane lines on live frames
* Provides **voice alerts** if any lane is missing
* Built with **OpenCV**, **NumPy**, **Tkinter**, and **pyttsx3**

### 🧠 Outcome:

A fully functional desktop application that detects lanes in real time and audibly alerts drivers when one or both lanes are not visible.

---

## ✅ 2. Plant Leaf Disease Detection System

### 📌 Objective:

To build a deep learning model that detects plant leaf diseases from image inputs, providing accurate classifications to help farmers take preventive action and improve crop yield.

### 🔍 Key Features:

* Utilizes **CNN (Convolutional Neural Network)** for image classification
* Supports over 38 plant diseases using the **PlantVillage dataset**
* Preprocessing includes normalization and augmentation
* Integrated with a **Gradio-based web app** for user-friendly disease prediction
* Delivers instant results from uploaded leaf images

### 🧠 Outcome:

An AI-based system that achieved high classification accuracy and is deployable as a web tool to assist the agriculture sector.

---

## ✅ 3. Summer Heatwaves Mobile Alert System

### 📌 Objective:

To predict and alert users about potential heatwave conditions across major Indian cities using historical seasonal temperature data. The goal is to mitigate heat-related health risks during extreme summers.

### 🔍 Key Features:

* Trained using a **Random Forest Classifier** on IMD temperature datasets
* Flask backend serves prediction data
* Kivy-based mobile app with dynamic UI
* Provides **audio and visual alerts** when heatwave is predicted
* Interactive mobile interface for checking heatwave risks city-wise

### 🧠 Outcome:

A complete AI pipeline integrated with mobile UI that gives timely alerts for heatwave conditions, useful for urban safety planning.

---

## 🛠️ Tech Stack Used

* **Languages:** Python
* **Libraries & Frameworks:**

  * OpenCV, NumPy, Tkinter, pyttsx3
  * TensorFlow/Keras, Scikit-learn, Pandas
  * Flask (Backend API)
  * Kivy (Mobile UI)
  * Gradio (Web Interface)
* **Tools:** Jupyter Notebook, VS Code

---

## 🛠️ Installation Guide

1. Clone the Repository

```bash
git clone https://github.com/your-username/next24tech-ai-ml-projects.git
cd next24tech-ai-ml-projects
```

2. Install Required Packages

```bash
pip install -r requirements.txt
```

3. To Run Each Project:

* **Task 1:**

  ```bash
  python task-1.py
  ```

* **Task 2:**
  Open Jupyter Notebook and run `plant_disease_detection.ipynb`
  Or launch Gradio Web App after training:

  ```python
  gr.Interface(...).launch()
  ```

* **Task 3:**
  Start backend:

  ```bash
  cd backend
  python app.py
  ```

  Start mobile app:

  ```bash
  cd ../mobile_app
  python main.py
  ```

---

## 📽️ Results & Demos

| Task                | Description                                        | Output                        |
| ------------------- | -------------------------------------------------- | ----------------------------- |
| Road Lane Detection | Detects and speaks warnings when lanes are missing | ✅ Real-time voice feedback    |
| Plant Leaf Disease  | Classifies leaf images using deep learning         | ✅ Gradio demo interface       |
| Heatwave Alert      | City-wise prediction and mobile alert              | ✅ Sound + animated warning UI |

---

## ✅ Conclusion

The **Next24tech AI/ML Internship** was a powerful learning experience that allowed me to:

* Apply machine learning and deep learning in real scenarios
* Build complete pipelines from data to deployment
* Develop real-time applications using both desktop and mobile interfaces
* Gain confidence in using libraries like OpenCV, TensorFlow, and Kivy

Each task strengthened my understanding of AI’s potential in **transport**, **agriculture**, and **climate risk management**.

---

## 📧 Contact

**Sampathirao Kavya**

AI/ML Developer Intern

Email: [kavs14345@gmail.com](mailto:kavs14345@gmail.com)

College: JNTU-GV University

Intern ID: NIP/2025/05A001

Mentor: *Next24tech Technologies Pvt. Ltd.*
