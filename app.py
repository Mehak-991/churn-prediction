import pandas as pd
from flask import Flask, request, render_template, session, redirect, url_for
import pickle
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'churnpredict_secret_key_2026'

# ---- Admin Credentials ----
ADMIN_EMAIL = "missmehak@gmail.com"
ADMIN_PASSWORD = "12345"

# Load original dataset and model
df_1 = pd.read_csv("first_telc.csv")
model = pickle.load(open("model.sav", "rb"))

# Clean and prepare original dataset
df_1['tenure'] = pd.to_numeric(df_1['tenure'], errors='coerce').fillna(0).astype(int)
labels = [f"{i} - {i + 11}" for i in range(1, 72, 12)]
df_1['tenure_group'] = pd.cut(df_1['tenure'], range(1, 80, 12), right=False, labels=labels)
df_1.drop(columns=['tenure'], inplace=True)

# Global list to store contact form messages
admin_messages = []

# ========== PUBLIC ROUTES ==========

@app.route("/")
def loadPage():
    empty_values = {f"query{i}": "" for i in range(1, 20)}
    return render_template("home.html", output1="", output2="", **empty_values)

@app.route("/", methods=['POST'])
def predict():
    # Check if this is a contact form submission
    if 'contact_submit' in request.form:
        new_msg = {
            'name': f"{request.form.get('first_name', '')} {request.form.get('last_name', '')}".strip(),
            'email': request.form.get('email', ''),
            'phone': request.form.get('phone', ''),
            'date': datetime.now().strftime("%B %d, %Y at %I:%M %p"),
            'message': request.form.get('message', '')
        }
        # Insert at the beginning so newest messages appear on top
        admin_messages.insert(0, new_msg)

        # Reload the page with empty form and a success flag
        empty_values = {f"query{i}": "" for i in range(1, 20)}
        return render_template("home.html", output1="", output2="", contact_success=True, **empty_values)

    # Otherwise, it is a churn prediction submission
    input_data = [request.form.get(f'query{i}', '') for i in range(1, 20)]

    new_df = pd.DataFrame([input_data], columns=[
        'SeniorCitizen', 'MonthlyCharges', 'TotalCharges', 'gender',
        'Partner', 'Dependents', 'PhoneService', 'MultipleLines', 'InternetService',
        'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport',
        'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling',
        'PaymentMethod', 'tenure'
    ])

    # Preprocess new input
    new_df['tenure'] = pd.to_numeric(new_df['tenure'], errors='coerce').fillna(0).astype(int)
    new_df['tenure_group'] = pd.cut(new_df['tenure'], range(1, 80, 12), right=False, labels=labels)
    new_df.drop(columns=['tenure'], inplace=True)

    # Combine with full data
    df_combined = pd.concat([df_1, new_df], ignore_index=True)

    # One-hot encode
    cat_cols = [
        'gender', 'SeniorCitizen', 'Partner', 'Dependents', 'PhoneService',
        'MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup',
        'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies',
        'Contract', 'PaperlessBilling', 'PaymentMethod', 'tenure_group'
    ]
    df_dummies = pd.get_dummies(df_combined[cat_cols])

    # Extract only new input row
    input_features = df_dummies.tail(1)

    # Align input with model's expected features
    if hasattr(model, 'feature_names_in_'):
        expected_cols = model.feature_names_in_
    else:
        expected_cols = input_features.columns  # fallback

    # Add any missing columns
    for col in expected_cols:
        if col not in input_features.columns:
            input_features[col] = 0

    # Reorder columns
    input_features = input_features[expected_cols]

    # Predict
    prediction = model.predict(input_features)[0]
    probability = model.predict_proba(input_features)[0][1]

    output1 = "This customer is likely to be churned!!" if prediction == 1 else "This customer is likely to continue!!"
    output2 = f"Confidence: {probability * 100:.2f}%"

    return render_template('home.html',
                           output1=output1,
                           output2=output2,
                           **{f"query{i}": request.form.get(f"query{i}", "") for i in range(1, 20)})

# ========== ADMIN ROUTES ==========

@app.route("/admin", methods=['GET', 'POST'])
def adminLogin():
    # If admin is already logged in, show the dashboard
    if session.get('is_admin'):
        return render_template("home.html", is_admin=True, admin_messages=admin_messages, output1="", output2="",
                               **{f"query{i}": "" for i in range(1, 20)})

    # Handle login form submission
    error = ""
    if request.method == 'POST':
        email = request.form.get('admin_email', '')
        password = request.form.get('admin_password', '')
        if email == ADMIN_EMAIL and password == ADMIN_PASSWORD:
            session['is_admin'] = True
            return redirect(url_for('adminLogin'))
        else:
            error = "Invalid email or password. Please try again."

    # Show login page
    return render_template("home.html", show_admin_login=True, admin_login_error=error, output1="", output2="",
                           **{f"query{i}": "" for i in range(1, 20)})

@app.route("/admin/logout")
def adminLogout():
    session.pop('is_admin', None)
    return redirect(url_for('loadPage'))

if __name__ == "__main__":
    app.run(debug=True)
