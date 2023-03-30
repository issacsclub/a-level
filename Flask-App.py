# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 21:05:40 2023

@author: Administrator
"""

# Import required libraries
from flask import Flask, request, jsonify

# Initialize Flask app
app = Flask(__name__)

# Define initial event details
event = {
    'name': 'My Event',
    'date': '2023-05-01',
    'location': 'Johannesburg',
    'status': 'Pending',
    'signatories': {
        'Department Head': False,
        'Finance Manager': False,
        'CEO': False
    }
}

# Define route for getting event details
@app.route('/event', methods=['GET'])
def get_event():
    return jsonify(event)

# Define route for updating signatory status
@app.route('/sign', methods=['POST'])
def sign_event():
    data = request.get_json()
    signatory = data['signatory']
    if signatory in event['signatories']:
        event['signatories'][signatory] = True
        if all(event['signatories'].values()):
            event['status'] = 'Approved'
        return jsonify({'message': f'{signatory} has signed.'})
    else:
        return jsonify({'message': f'{signatory} is not a valid signatory.'})

# Run Flask app
if __name__ == '__main__':
    app.run()
