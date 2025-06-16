import joblib
import numpy as np
import os
import requests

model_path=os.path.abspath(os.path.join(os.path.dirname(__file__),'..','model','heatwave_model.pkl'))
model=joblib.load(model_path)

def predict_heatwave(data):
    features=np.array([[
        data['annual'],data['jan_feb'],data['mar_may'],
        data['jun_sep'],data['oct_dec']
    ]])
    return int(model.predict(features)[0])

def get_live_temperature(city="Delhi"):
    api_key="0e639a8e4ab00817f0bc1ed630c2b3e4" 
    url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=0e639a8e4ab00817f0bc1ed630c2b3e4&units=metric"

    response=requests.get(url)
    if response.status_code==200:
        data=response.json()
        return data["main"]["temp"]
    else:
        return None

# FUNCTION TO PREDICT USING LIVE TEMP
def predict_from_live_temp(city="Delhi"):
    temp=get_live_temperature(city)
    if temp is None:
        return {"error": "Could not fetch live temperature"}

    # Here we assume other seasonal values are average, and only MAR-MAY gets live temp
    dummy_data={
        "annual": temp,         
        "jan_feb": temp - 2,  
        "mar_may": temp,
        "jun_sep": temp + 2,
        "oct_dec": temp - 1
    }

    result=predict_heatwave(dummy_data)
    return {
        "city": city,
        "temperature": temp,
        "heatwave": bool(result)
    }
