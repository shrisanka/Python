import json

def lambda_handler(event, context):
    try:
        # Parse input data from the Lambda event
        body = json.loads(event['body'])
        pounds = float(body['pounds'])

        # Convert pounds to kilograms
        kilograms = pounds * 0.453592

        # Prepare the response
        response = {
            'statusCode': 200,
            'body': json.dumps({'kilograms': kilograms})
        }
    except ValueError as e:
        # Handle invalid input
        response = {
            'statusCode': 400,
            'body': json.dumps({'error': str(e)})
        }
    except Exception as e:
        # Handle other errors
        response = {
            'statusCode': 500,
            'body': json.dumps({'error': 'An internal server error occurred.'})
        }

    return response
