import json


def get_responses(check_amount):

    with open('./TJSIMResponses/AllResponses.json', 'r') as file:
        data = json.load(file)

    for group_number, transaction in enumerate(data['items']):
        if check_amount == transaction['amount']:
            response_message = transaction
    
    return response_message