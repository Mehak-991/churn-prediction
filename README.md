# 📊 Customer Churn Prediction Web App

This project is a complete **machine learning pipeline and deployment system** to predict whether a telecom customer is likely to **churn or continue**. It uses a **Random Forest Classifier** trained with **SMOTEENN** to handle class imbalance, and a **Flask web app** for deployment.

---

## 🚀 Project Highlights

- 📂 Dataset: Downloaded from **Kaggle** using an API key  
- 🧠 Model: `RandomForestClassifier` trained on **balanced data** using **SMOTEENN**  
- 🏷️ Target: Predict whether a customer will **churn** (Yes/No)  
- 🌐 Deployment: Interactive **Flask-based web interface**  
- ✅ Output: Whether a customer will churn, along with a **confidence score**

---

## 📁 Dataset

The dataset used was downloaded from Kaggle via an API key. It contains features such as:

- `gender`, `SeniorCitizen`, `Partner`, `Dependents`
- `tenure`, `MonthlyCharges`, `TotalCharges`
- `InternetService`, `Contract`, `PaymentMethod`
- ... and many more relevant attributes.

**Tenure** is converted into `tenure_group` using interval binning for improved feature representation.

---

## 🧠 Model Building (`model_training.py`)

- The dataset is cleaned and prepared.
- **SMOTEENN** is applied to balance the dataset.
- A **Random Forest Classifier** is trained with:
  - `n_estimators=100`
  - `max_depth=6`
  - `min_samples_leaf=8`
- Evaluation metrics include:
  - Accuracy
  - Classification report
  - Confusion matrix

> The final model is saved using `pickle` and used in deployment.

---

## 🌐 Deployment (`app.py`)

- Built with **Flask**
- Accepts user input via a web form
- Preprocesses the input to match model features
- Predicts whether the customer is likely to churn
- Shows **prediction and confidence score**

### 🧾 Example Output

> ✅ **This customer is likely to continue!**  
> 🔒 **Confidence: 85.27%**

---

## 🛠 Requirements

All dependencies are listed in the `requirements.txt` file.

### ✅ Installing Required Packages

```bash
pip install -r requirements.txt
▶️ Running the App
Clone the repository and place your trained model.sav file in the root directory.

Make sure the dataset first_telc.csv is also in the same directory.

Launch the Flask app:
python app.py

📁 Project Structure
├── app.py                  # Flask web app
├── model.sav               # Trained Random Forest model
├── model_training.py       # Script for training the model
├── first_telc.csv          # Preprocessed dataset
├── requirements.txt        # Python dependencies
├── templates/
│   └── home.html           # HTML form for user input

📌 Notes
The feature alignment during prediction ensures that all expected columns match those used during model training.

The output includes a confidence score, using predict_proba.
🧪 Technologies Used
Python 3.10+

Pandas

Scikit-learn

Imbalanced-learn

Flask





this is my project understand it for helping me with everything 

Project Explanation: Customer Churn Prediction System
1. Project Overview
The Customer Churn Prediction System is a machine learning–based web application designed to predict whether a customer is likely to leave a service. The system integrates a trained prediction model with a backend API to provide real-time churn predictions based on user input.
The primary objective of the project is to assist businesses in identifying at-risk customers and taking preventive actions to improve customer retention.
2. Dataset Information
* Source: Public dataset (Kaggle – Telco Customer Churn dataset)
* File Used: `WA_Fn-UseC_-Telco-Customer-Churn.csv`
* Data Storage: Stored locally within the project repository
Dataset Features
The dataset includes:
* Customer demographics (gender, senior citizen, etc.)
* Account details (tenure, contract type)
* Service usage (internet service, phone service)
* Billing information (monthly charges, total charges)
* Target Variable: `Churn` (Yes/No)
3. Data Processing Pipeline
The dataset undergoes preprocessing before model training and prediction:
* Handling missing values
* Encoding categorical variables (e.g., Yes/No → 1/0)
* Feature selection and transformation
* Conversion into numerical format for model compatibility
Libraries used:
* Pandas
* NumPy
* Scikit-learn
4. Machine Learning Model
* Model is trained using classification algorithms (e.g., Logistic Regression / Random Forest)
* Model learns patterns from historical customer data
* Trained model is saved as:
   * File: `model.pkl`
Model Function
* Input: Processed customer data
* Output: Prediction (Churn / No Churn)
5. Backend System (Flask API)
Main File
* `app.py` → Core backend file
Backend Responsibilities
* Handle user requests
* Process input data
* Load trained model (`model.pkl`)
* Perform prediction
* Return results
6. API Workflow
Step-by-Step Flow
1. User enters customer details in frontend
2. Frontend sends request to backend API
3. Backend receives JSON data
4. Data is preprocessed
5. Model generates prediction
6. Result is returned to frontend
Example
Request:

```
{
  "tenure": 10,
  "MonthlyCharges": 80,
  "Contract": "Month-to-month"
}
```

Response:

```
{
  "prediction": "No Churn"
}
```

7. System Architecture (Conceptual)

```
Frontend (User Input)
        ↓
Flask API (app.py)
        ↓
Data Preprocessing
        ↓
ML Model (model.pkl)
        ↓
Prediction Output
        ↓
Frontend Display
```

8. Tools and Technologies
ComponentTechnologyProgrammingPythonBackendFlaskML LibraryScikit-learnData ProcessingPandas, NumPyModel StoragePickle (.pkl)IDEVS Code
9. Project Milestones
Milestone 1: Dataset Collection & Setup
* Collected churn dataset from Kaggle
* Stored dataset in project directory
* Performed initial data cleaning and exploration
Milestone 2: Data Preprocessing & Model Training
* Handled missing values and inconsistencies
* Encoded categorical variables
* Trained machine learning model
* Saved model as `model.pkl`
Milestone 3: Backend Development
* Developed Flask application (`app.py`)
* Created REST APIs for prediction
* Integrated model with backend
Milestone 4: API Integration & Testing
* Connected frontend with backend APIs
* Tested request-response flow
* Ensured real-time prediction functionality
Milestone 5: Final System & Optimization
* Improved prediction accuracy
* Optimized API performance
* Prepared system for deployment
10. Key Achievements
* Successfully built an end-to-end ML system
* Implemented real-time prediction using APIs
* Integrated dataset, model, and backend
* Achieved smooth communication between components
11. Challenges Faced
* Data preprocessing complexity
* Handling categorical variables
* Ensuring consistent input format for prediction
* API integration issues
12. Future Scope
* Deploy application on cloud (AWS/Heroku)
* Improve model accuracy using advanced algorithms
* Add user authentication system
* Enhance UI/UX for better usability