---

# 🌿 Plant Leaf Disease Detection System using AI Algorithms

This project aims to assist farmers and agricultural professionals in identifying plant leaf diseases using artificial intelligence. It uses a Convolutional Neural Network (CNN) to classify images of plant leaves as healthy or diseased, enabling early intervention and improved crop yield.

## 📌 Table of Contents

* [Overview](#-overview)
* [Features](#-features)
* [Tech Stack](#-tech-stack)
* [Dataset](#-dataset)
* [Model Architecture](#-model-architecture)
* [Installation](#-installation)
* [How to Run](#-how-to-run)
* [Gradio Web App](#-gradio-web-app)
* [Screenshots](#-screenshots)
* [Results](#-results)
* [Future Scope](#-future-scope)
* [Contributors](#-contributors)
* [License](#-license)

---

## 📖 Overview

The **Plant Leaf Disease Detection System** is built using deep learning to automatically classify plant leaf images into healthy or diseased categories. This system helps improve agricultural decision-making by providing instant disease diagnosis through an easy-to-use web interface.

---

## ✅ Features

* Detects diseases in plant leaves from images
* Supports over 38 classes (e.g., Tomato blight, Apple rust)
* Data preprocessing and augmentation
* Trained CNN model using TensorFlow/Keras
* Gradio-powered web interface for predictions
* Works with any JPG/PNG image upload

---

## 🛠 Tech Stack

* Python 3.10+
* TensorFlow / Keras
* NumPy, Matplotlib, Scikit-learn
* OpenCV (optional for visualization)
* Gradio (for web app)
* Jupyter Notebook / VS Code

---

## 📂 Dataset

* **Source**: [PlantVillage Dataset](https://www.kaggle.com/datasets/emmarex/plantdisease)
* Contains 50,000+ images across 38 plant disease and healthy categories
* Used `ImageDataGenerator` to perform train-validation split (80-20)
* Image size: resized to `128x128` for faster processing

---

## 🧠 Model Architecture

The model is a **Convolutional Neural Network (CNN)** with the following layers:

* Conv2D + ReLU + MaxPooling (x2)
* Flatten
* Dense layer (ReLU)
* Output Dense layer (Softmax)

**Loss Function**: Categorical Crossentropy
**Optimizer**: Adam
**Epochs**: 5
**Accuracy**: \~95%+ on validation data (varies)

---

## 💻 Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/plant-leaf-disease-detection.git
cd plant-leaf-disease-detection

# Install dependencies
pip install -r requirements.txt
```

Ensure the dataset is extracted in the correct structure before proceeding.

---

## 🚀 How to Run

1. Place the `PlantVillage` folder in your project directory.
2. Run the Jupyter notebook step-by-step or execute `main.py`.
3. The model will train and save as `Plant_disease_model.h5`.

To split the dataset:

```bash
# Inside notebook
!python split_dataset.py
```

To train the model:

```bash
# Inside notebook
model.fit(train_gen, validation_data=val_gen, epochs=5)
```

---

## 🌐 Gradio Web App

After training, run the Gradio interface:

```python
import gradio as gr
from keras.models import load_model
import numpy as np
from tensorflow.keras.preprocessing import image

model = load_model("Plant_disease_model.h5")
class_names = train_gen.class_indices
class_names = list(class_names.keys())

def predict(img):
    img = img.resize((128, 128))
    img = image.img_to_array(img) / 255.0
    img = np.expand_dims(img, axis=0)
    pred = model.predict(img)[0]
    return {class_names[i]: float(pred[i]) for i in range(len(class_names))}

gr.Interface(fn=predict, inputs="image", outputs="label", title="🌿 Plant Disease Detector").launch()
```

---

## 🖼 Screenshots

![Output](https://github.com/user-attachments/assets/c869fc43-e182-441e-8160-4cb2885e6827)


---

## 📈 Results

* Achieved high accuracy on validation data
* Detected multiple plant diseases with high confidence
* User interface allows real-time leaf image prediction

---
## Demo Video:


https://github.com/user-attachments/assets/e9687750-ce1f-4d77-93ba-2577ccac6cf0



---
## 🔮 Future Scope

* Deploy model as Android/web app
* Support voice-based disease diagnosis
* Add suggestions for pesticides or remedies based on disease
* Multilingual interface for farmers

---

## 👩‍💻 Contributors

* **Sampathirao Kavya** – AI/ML Developer
  *Intern, Next24tech Technology AICTE Internship Program*

---
