## 🌞 Summer Heatwaves Mobile Alert System – Task 3 

### 🔍 Project Overview

This project is an AI-powered system designed to **predict and alert users** about potential heatwaves across major Indian cities using seasonal temperature patterns. It helps the public stay safe during extreme summer conditions by providing timely alerts through a **mobile-friendly app interface**.

---

### 🚀 Features

* 🔎 **Live Heatwave Prediction** for selected cities
* 📊 Trained ML model on IMD seasonal temperature data
* 🧠 Uses **Random Forest Classifier** to predict heatwave conditions
* 🗂️ Flask-based backend to serve predictions
* 📱 Kivy-based mobile app with interactive UI
* 🔔 **Sound and animated alerts** for heatwave warnings
* 🌐 Real-time integration of trained model with mobile front-end

---

### 📁 Project Structure

```
SummerHeatwaveAlertSystem/
│
├── train_model.py                # Trains ML model using IMD dataset
├── TEMP_ANNUAL_SEASONAL_MEAN.csv # Historical temperature data
├── model/
    ├── heatwave_model.pkl           # Trained model file
│
├── backend/
│   ├── app.py                   # Flask API for live predictions
│   ├── utils.py                 # Loads model & predicts from backend
│
├── mobile_app/
│   ├── main.py                  # Kivy-based mobile UI
│   ├── alert.wav                # Sound alert for heatwaves
│
├── requirements.txt             # Project dependencies
└── README.md                    # You're here!
```

---

### 🧠 ML Model Info

* **Algorithm**: Random Forest Classifier
* **Target Variable**: Heatwave (1 if MAR-MAY temperature > 28.5°C)
* **Features Used**: Annual, Jan-Feb, Mar-May, Jun-Sep, Oct-Dec seasonal temperatures
* **Model File**: `heatwave_model.pkl` (used by Flask backend)

---

### 📱 Mobile App UI

* Built with **Kivy**
* Users select a city from a dropdown
* On checking, receives alert from backend:

  * ✅ Normal year = green alert
  * 🔥 Heatwave = red alert + sound + animation
* Responsive layout with theme-colored buttons and dynamic messages

---

### ⚙️ How to Run the Project

1. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

2. **Train the model (Optional, already provided)**

   ```bash
   python train_model.py
   ```

3. **Start Flask Backend**

   ```bash
   cd backend
   python app.py
   ```

4. **Run Mobile App**

   ```bash
   cd ../mobile_app
   python main.py
   ```

---

### 🔉 Note on Sound

* `alert.wav` must be placed in `mobile_app/` folder
* Uses `pygame.mixer` for reliable playback across systems

---

### 📌 Dependencies

* `pandas`, `scikit-learn`, `flask`, `kivy`, `pygame`, `requests`, `joblib`

---

### ✅ Outcome

* The system can **accurately flag heatwave years**
* Simulates a real-world alerting platform for climate risk mitigation
* Fully functional backend + mobile UI interaction pipeline

---

### 👩‍💻 Developed By

**Sampathirao Kavya**

Intern, AI-ML Development | Next24Tech Internship

June 2025
