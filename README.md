# Spam-Ham Detection Web App

This repository contains a Flask web application that detects whether a given message is "Spam" or "Ham" (not spam). The app uses a pre-trained machine learning model for spam classification.

## Features:
- Detects whether a message is spam or ham based on its content.
- Built with Flask, a lightweight Python web framework.
- Uses a pre-trained model loaded with `joblib` to classify messages.

## Prerequisites:
Before running the application, ensure you have the following installed:
- Python 3.6 or later
- pip (Python package manager)

## Setup Instructions:

1. Clone the repository:
  git clone https://github.com/yourusername/spam-ham-detection.git
  cd spam-ham-detection

2. Install the required dependencies:
  pip install -r requirements.txt

3. Run the Flask app:
  python app.py

4. Open the web app:
Once the Flask app is running, open your browser and navigate to http://127.0.0.1:5000/ to access the prediction interface.

## Usage:
Input the message text into the provided form.
Click the "Predict" button to classify the message as either "Spam" or "Ham."

## Example Output:
After submitting the message, the web app will display:
Spam or Ham: The classification result for the message, either "Spam" or "Ham."

## Notes:
The app assumes that the pre-trained model is properly loaded and the input message is correctly formatted.
The app will return an error message if the model encounters issues during prediction.
