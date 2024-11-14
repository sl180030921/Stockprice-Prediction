from flask import Flask, request, render_template
import numpy as np
from tensorflow.keras.models import load_model  # Use Keras load_model for .h5 files

# Load the pre-trained model
model = load_model("best_stock_model.h5")

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    stock_ticker = request.form.get('ticker')
    
    # Here, add code to fetch data for `stock_ticker`, preprocess, and make predictions
    prediction = np.random.random()  # Placeholder for actual model prediction
    return render_template('index.html', prediction_text=f'Predicted Price for {stock_ticker}: {prediction}')

if __name__ == "__main__":
    app.run(debug=True)
