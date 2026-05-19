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





