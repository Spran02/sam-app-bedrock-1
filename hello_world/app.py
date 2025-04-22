import json
import datetime

def lambda_handler(event, context):
    print("=== Received Event ===")
    print(json.dumps(event))  # Log the full event for debugging

    agent = event.get('agent')
    actionGroup = event.get('actionGroup')
    function = event.get('function')
    raw_parameters = event.get('parameters', [])

    # Convert list-based parameters to a dictionary
    parameters = {param["name"]: param["value"] for param in raw_parameters}

    print("=== Extracted Parameters ===")
    print(parameters)  # Debugging print

    # Handling different function calls
    if function == "get_time":
        result = get_utc_time()
    elif function == "add_two_numbers":
        num1 = parameters.get("number1")
        num2 = parameters.get("number2")

        print(f"Number 1: {num1}, Number 2: {num2}")  # Debugging

        try:
            num1, num2 = float(num1), float(num2)
            result = {"sum": num1 + num2}
        except ValueError:
            result = {"error": "Invalid parameters. Please provide two numbers."}
    else:
        result = {"error": f"Unknown function: {function}"}

    responseBody = {"TEXT": {"body": json.dumps(result)}}

    action_response = {
        'actionGroup': actionGroup,
        'function': function,
        'functionResponse': {
            'responseBody': responseBody
        }
    }

    dummy_function_response = {
        'response': action_response,
        'messageVersion': event.get('messageVersion')
    }

    print("=== Final Response ===")
    print(json.dumps(dummy_function_response, indent=2))  # Log final response

    return dummy_function_response





def get_utc_time():
    return {"utc_time": datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")}
