import json
import uuid

def get_responses(request_body):

    check_amount = request_body['amount']

    with open('./TJSIMResponses/AllResponses.json', 'r') as file:
        data = json.load(file)

    for group_number, transaction in enumerate(data['items']):
        if check_amount == transaction['amount']:
            response_message = transaction
            # Set response to match request values
            response_message["store"] = request_body["store"]
            response_message["pos"] = request_body["pos"]

            response_message["reference"] = request_body["reference"]




    return response_message