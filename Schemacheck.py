from flask import Flask, request, jsonify

from jsonschema import validate

def check_schema(request_body):

    request_schema  = {
    "type": "object",
    "properties": {
        "tran": {
        "type": "string",
        "enum": ["PURCHASE", "RETURN"]
        },
        "amount": {
        "type": "integer",
        "minimum": 0
        },
        "reference": {
        "type": "string",
        "format": "uuid"
        },
        "pos": {
        "type": "string",
        "minLength": 8,
        "maxLength": 8
        },
        "store": {
        "type": "string",
        "minLength": 15,
        "maxLength": 15
        },
        "chain": {
        "type": "string"
        },
        "receiptRequired": {
        "type": "boolean"
        }
    },
    "required": ["tran", "amount", "reference", "pos", "store", "chain"]
    }


    try:
        validate(instance=request_body, schema=request_schema)
        # Process the valid request data here
        return True
    except Exception as e:
        return jsonify({"error": "Invalid request body", "details": str(e)}), 400