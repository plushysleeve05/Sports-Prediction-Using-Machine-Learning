from flask import Flask, render_template, request
import pickle
import joblib


app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    
    return render_template('homepage.html')
    

@app.route('/', methods=['POST'])
def predict():
    with open("C:\\Users\\ayoba\\OneDrive - Ashesi University\\Year 2 sem 2 fall\\AI\\mid sem project\\group9_flask_deployment\\webpages\\final_xgb_model.pk1", "rb") as model_file:
        model = pickle.load(model_file)

    feature1 = float(request.form['potential'])
    feature2 = float(request.form['value_eur'])
    feature3 = float(request.form['age'])
    feature4 = float(request.form['release_clause_eur'])
    feature5 = float(request.form['dribbling'])
    feature6 = float(request.form['shooting'])
    feature7 = float(request.form['wage_eur'])

    data = [[feature1, feature2, feature3, feature4, feature5, feature6, feature7]]

    scalerO = joblib.load("C:\\Users\\ayoba\\OneDrive - Ashesi University\\Year 2 sem 2 fall\\AI\\mid sem project\\group9_flask_deployment\\webpages\\scaler.pkl")

    scaled_data = scalerO.transform(data)
    prediction = model.predict(scaled_data)
    
    return render_template('homepage.html', prediction=prediction)

if __name__ == "__main__":
    app.run(port=3000, debug= True)
