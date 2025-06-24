# ⚽ Group 9 – Sports Player Performance Prediction

## 🚀 Overview

This project uses machine learning to predict the performance or value of football players based on historical and profile data. It involves cleaning raw player data, selecting relevant features, training a regression model (XGBoost), and deploying a web-based prediction interface using Flask.

The project demonstrates a full **ML pipeline**, from data preprocessing and model evaluation to deployment.

---

## 🧠 Features

- Load and clean player data from CSV files  
- Remove features with excessive missing values and irrelevant columns  
- Encode categorical variables for modeling  
- Separate data into numerical and textual features  
- Train an XGBoost model with cross-validation and hyperparameter tuning  
- Save trained model and scaler using `pickle`/`joblib`  
- Deploy a web app for user input and prediction using Flask  

---

## 🏗️ File Structure

| File/Folder | Description |
|-------------|-------------|
| `group9_sportsprediction.py` | Main Python script with preprocessing and training pipeline |
| `Group9_SportsPrediction.ipynb` | Jupyter notebook version of pipeline |
| `final_xgb_model.pkl` | Trained XGBoost regression model |
| `scaler.pkl` | Scaler used for preprocessing features |
| `app.py` | Flask web app for predictions |
| `players_21.csv`, `players_22.csv` | Raw player datasets |
| `templates/homepage.html` | HTML interface for user input |
| `static/pic.jpg` | Image used in the UI |

---

## 🔁 How It Works

1. Load the CSV dataset (`players_21.csv`) using Pandas.  
2. Drop columns with >30% missing data.  
3. Remove irrelevant columns like URLs, names, and IDs.  
4. Encode categorical values using `LabelEncoder`.  
5. Train the XGBoost regressor on selected numeric features.  
6. Evaluate the model using Mean Absolute Error (MAE) and other metrics.  
7. Save the model and scaler for reuse.  
8. Use Flask to create a web interface where users can input values and receive predictions.  

---

## 📂 How to Run

### 🔧 Local Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/GROUP9_SPORTSPREDICTION.git
   cd GROUP9_SPORTSPREDICTION

   pip install -r requirements.txt

   python app.py

   http://127.0.0.1:5000/


## Sample Output 
Input: 
- Age: 25
- Height: 180 cm
- Weight: 75 kg
- Position: CM
- League: Premier League

Output:
→ Predicted Player Value: €7,300,000

## Concepts Demonstrated 
Data cleaning – threshold-based removal of nulls

Feature engineering – encoding and separation of numerical/textual data

Model training – XGBoost with cross-validation

Model evaluation – MAE, MSE, and error scoring

Deployment – lightweight Flask application with web input


   


