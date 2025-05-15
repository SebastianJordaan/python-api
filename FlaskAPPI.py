# from flask import Flask
from flask import Flask, request, jsonify
from jsonschema import validate
import json


import GetResult
import Schemacheck

app = Flask(__name__)
# Configure Flask to not sort JSON keys
app.json.sort_keys = False

@app.route('/hello')
def home():
    return {"message": "Hello, Flask API!"}



@app.route('/tjpos/v1/card', methods=['POST'])
def tran_sim():

    data = request.get_json()
    print(data)
    # Function to check schema
    schema_result = Schemacheck.check_schema(data)
    if(schema_result != True):
        return schema_result
    print('Chema result = ')
    print(schema_result)

    amout = data['amount']



    # Function to fetch response
    hardcoded_response = GetResult.get_responses(amout)

    print(hardcoded_response)
    print(json.dumps(hardcoded_response, indent=4))
    
    # return hardcoded_response
    # return json.loads(json.dumps(hardcoded_response))
    # return json.dumps(hardcoded_response, indent=4)
    return jsonify(hardcoded_response)
    # return {"message": "Hello, Flask API!"}

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=5000, debug=True) # Enable debug mode for development