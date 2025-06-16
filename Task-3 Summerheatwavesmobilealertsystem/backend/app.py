from flask import Flask, request, jsonify
from flask_cors import CORS
from utils import predict_heatwave,predict_from_live_temp

app=Flask(__name__)
CORS(app)

@app.route("/predict",methods=["POST"])
def predict():
    data=request.json
    temperature=data.get('temperature')
    prediction=predict_heatwave([temperature])
    return jsonify({"heatwave": bool(prediction)})

@app.route('/predict_live',methods=['GET'])
def predict_live():
    city=request.args.get('city','Delhi')
    result=predict_from_live_temp(city)
    return jsonify(result)

if __name__=="__main__":
    app.run(debug=True)