# from flask import Flask
from flask import Flask, request, jsonify
from jsonschema import validate

import GetResult
import Schemacheck

app = Flask(__name__)
# Configure Flask to not sort JSON keys
app.config['JSON_SORT_KEYS'] = False

@app.route('/hello')
def home():
    return {"message": "Hello, Flask API!"}



@app.route('/tjpos/v1/card', methods=['POST'])
def tran_sim():

    data = request.get_json()
    print(data)
    # Function to check schema
    schema_result = Schemacheck.check_schema(data)
    if(not schema_result):
        return jsonify({"error": "Invalid request body", "details": str(e)}), 400
    print('Chema result = ')
    print(schema_result)

    amout = data['amount']



    # Function to fetch response
    hardcoded_response = GetResult.get_responses(amout)

    return jsonify(hardcoded_response)
    # return {"message": "Hello, Flask API!"}

if __name__ == '__main__':
    app.run(debug=True)