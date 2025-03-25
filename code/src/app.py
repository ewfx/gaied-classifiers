from flask import Flask, render_template, request, jsonify
import subprocess
import pandas as pd
import os
import numpy as np

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
    
    # Paths to the output CSV files
    email_processing_file = 'app/DataFrames/output.csv'  # Email processing data
    duplicate_email_file = 'app/DataFrames/duplicate.csv'  # Duplicate email data
    
    data = {}

    # Check if the email processing file exists
    if os.path.exists(email_processing_file):
        df1 = pd.read_csv(email_processing_file)
        
        # Replace NaN values with empty strings or "N/A"
        df1 = df1.replace({np.nan: 'N/A'})
        
        data['email_processing_data'] = df1.to_dict(orient='records')
    else:
        data['email_processing_data'] = 'Error: Email processing data not found.'

    # Check if the duplicate email file exists
    if os.path.exists(duplicate_email_file):
        df2 = pd.read_csv(duplicate_email_file)
        
        # Replace NaN values with empty strings or "N/A"
        df2 = df2.replace({np.nan: 'N/A'})
        
        data['duplicate_email_data'] = df2.to_dict(orient='records')
    else:
        data['duplicate_email_data'] = 'Error: Duplicate email data not found.'
    
    # Return the combined data as JSON
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
