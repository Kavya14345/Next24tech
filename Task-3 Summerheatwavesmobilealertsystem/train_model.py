import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import os

#Load and preprocess data
df=pd.read_csv(r"Data/TEMP_ANNUAL_SEASONAL_MEAN.csv")
df.columns=df.columns.str.strip()
df=df.dropna()

# Convert temperature columns to float
temp_cols=['ANNUAL','JAN-FEB','MAR-MAY','JUN-SEP','OCT-DEC']
for col in temp_cols:
    df[col]=pd.to_numeric(df[col],errors='coerce')  # handles strings safely

df=df.dropna(subset=temp_cols)  # Drop rows where conversion failed

#Label heatwave years(if MAR-MAy temp>28.5 c)
df['Heatwave']=df['MAR-MAY'].apply(lambda x:1 if x>28.5 else 0)

#FEatures and target
X=df[temp_cols]
y=df['Heatwave']

#Train model
X_train,X_test,y_train,y_test=train_test_split(X,y,stratify=y)
model=RandomForestClassifier(random_state=42)
model.fit(X_train,y_train)

#Make sure model folder exists
os.makedirs("model",exist_ok=True)

#Save model
joblib.dump(model,r"model/heatwave_model.pkl")
print("Model trained and saved")