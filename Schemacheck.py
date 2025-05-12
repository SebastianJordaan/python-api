

from jsonschema import validate

def check_schema(request_body):

    request_schema  = {
    "type": "object",
    "properties": {
        "tran": {
        "type": "string",
        "enum": ["PURCHASE"]
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
        "type": "string"
        },
        "store": {
        "type": "string"
        },
        "chain": {
        "type": "string"
        },
        "receiptRequired": {
        "type": "boolean"
        }
    },
    "required": ["tran", "amount", "reference", "pos", "store", "chain", "receiptRequired"]
    }


    try:
        validate(instance=request_body, schema=request_schema)
        # Process the valid request data here
        return True
    except Exception as e:
        return False