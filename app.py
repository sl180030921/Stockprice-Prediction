from flask import Flask, request, render_template_string
import yfinance as yf
import numpy as np

# Initialize the Flask application
app = Flask(__name__)

# Define the HTML template
HTML_TEMPLATE = """
<!doctype html>
<html lang="en">
  <head>
    <title>Stock Price Prediction</title>
    <style>
      body { font-family: Arial, sans-serif; margin: 2em; }
      form { margin-bottom: 1em; }
      input[type=text] { padding: 0.5em; }
      input[type=submit] { padding: 0.5em; cursor: pointer; }
    </style>
  </head>
  <body>
    <h1>Stock Price Prediction</h1>
    <form method="post">
      <label for="ticker">Enter Stock Ticker:</label>
      <input type="text" id="ticker" name="ticker" required>
      <input type="submit" value="Predict">
    </form>
    {% if prediction %}
      <h3>Predicted Price for {{ ticker }}: ${{ prediction }}</h3>
    {% endif %}
  </body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def predict_stock():
    prediction = None
    ticker = None

    if request.method == "POST":
        ticker = request.form["ticker"]
        
        # Fetch historical data for the ticker using yfinance
        try:
            data = yf.download(ticker, period="5d")
            if data.empty:
                prediction = "Ticker not found or no data available."
            else:
                # Use the last available close price and simulate a prediction
                last_close = data['Close'].iloc[-1]
                prediction = round(last_close * np.random.uniform(0.95, 1.05), 2)
        except Exception as e:
            prediction = f"Error: {str(e)}"

    # Render HTML with prediction
    return render_template_string(HTML_TEMPLATE, prediction=prediction, ticker=ticker)

# Run the Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
