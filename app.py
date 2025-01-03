from flask import Flask, request, jsonify, render_template
import pandas as pd
import joblib

# Loading Models
model = joblib.load('model.pkl')
print("Model loaded successfully!")

# Initialising a Flask Application
app = Flask(__name__)

# Home Routing, Showcase Page
@app.route('/')
def home():
    return render_template('index.html')

# Predictive routing (API)
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        df = pd.DataFrame(data, index=[0])
        df = df[model.feature_names_in_]
        prediction = model.predict(df)
        result = "Sufficient" if prediction[0] == 1 else "Insufficient"
        return jsonify({'prediction': result})
    except Exception as e:
        return jsonify({'error': str(e)})

# Front-end button trigger prediction
@app.route('/submit', methods=['POST'])
def submit():
    try:
        data = request.form
        df = pd.DataFrame([{
            "blood_a": int(data['blood_a']),
            "blood_b": int(data['blood_b']),
            "blood_o": int(data['blood_o']),
            "blood_ab": int(data['blood_ab']),
            "location_centre": int(data['location_centre']),
            "location_mobile": int(data['location_mobile']),
            "type_wholeblood": int(data['type_wholeblood']),
            "type_apheresis_platelet": int(data['type_apheresis_platelet']),
            "type_apheresis_plasma": int(data['type_apheresis_plasma']),
            "type_other": int(data['type_other']),
            "social_civilian": int(data['social_civilian']),
            "social_student": int(data['social_student']),
            "social_policearmy": int(data['social_policearmy']),
            "donations_new": int(data['donations_new']),
            "donations_irregular": int(data['donations_irregular']),
            "donations_regular": int(data['donations_regular']),
        }])

        df = df[model.feature_names_in_]
        prediction = model.predict(df)
        result = "Sufficient" if prediction[0] == 1 else "Insufficient"
        return render_template('index.html', prediction=result, request=request)
    except Exception as e:
        return render_template('index.html', prediction=f"Error: {str(e)}", request=request)


# Starting a Flask Application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
