# app.py
from flask import Flask, render_template, request, jsonify
import subprocess
import pandas as pd
import time
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start-process', methods=['POST'])
def start_process():
    # Run the Python script
    process = subprocess.Popen(['python', 'app/main.py'])
    
    # Wait for the process to complete
    process.wait()
    
    # Path to the output CSV file
    output_file = 'app/DataFrames/output.csv'
    
    # Check if the file exists before trying to read it
    if os.path.exists(output_file):
        # Read the DataFrame
        df = pd.read_csv(output_file)
        # Return the DataFrame as JSON
        return df.to_json(orient='records')
    else:
        return 'Error: No data found or process failed.', 500

if __name__ == '__main__':
    app.run(debug=True)
