# from flask import Flask
from flask import Flask, request, jsonify
# from jsonschema import validate
# from flask_sqlalchemy import SQLAlchemy
import json


import GetResult
import Schemacheck
import SqlAlchemyInt

app = Flask(__name__)
# Configure Flask to not sort JSON keys
app.json.sort_keys = False

# ============================= Hello ===============================
@app.route('/hello')
def home():
    return {"message": "Hello, Flask API!"}


# ============================= POS Request ===============================
@app.route('/tjpos/v1/card', methods=['POST'])
def tran_sim():

    #fetch json body request
    data = request.get_json()
    
    # Function to check schema
    schema_result = Schemacheck.check_schema(data)
    # If schema check does not pass, return the error of the function
    if(schema_result != True):
        return schema_result

    # Commit request
    SqlAlchemyInt.create_tran_record_request(data)
    
    # Function to fetch response
    hardcoded_response = GetResult.get_responses(data)

    # Commit response
    SqlAlchemyInt.create_tran_record_response(hardcoded_response)

    return jsonify(hardcoded_response)


if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=5000, debug=True) # Enable debug mode for development