import sys
import numpy as np
import pickle
from flask import Flask, request, render_template
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences


sys.stdout.reconfigure(encoding='utf-8')

app = Flask(__name__)

model = load_model('model.h5')
with open('tokenizer.pkl', 'rb') as handle:
    tokenizer = pickle.load(handle)

max_length = 100

@app.route('/')
def home():

    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    message = request.form['message']
    try:
        message = message.encode('utf-8', 'ignore').decode('utf-8')  
    except UnicodeEncodeError as e:
        print(f"UnicodeEncodeError: {e}")
        return render_template('index.html', prediction_text="Encoding error occurred. Please use plain text.")
    
    sequence = tokenizer.texts_to_sequences([message])
    padded = pad_sequences(sequence, maxlen=max_length, padding='post')
    prediction = model.predict(padded)[0][0]
    result = "Spam" if prediction > 0.5 else "Ham"
    return render_template('index.html', prediction_text=f'The message is: {result}')

if __name__ == '__main__':
    app.run(debug=True)
