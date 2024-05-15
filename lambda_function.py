import json

def lambda_handler(event, context):
    x = 5
    y = 10

    def suma(a, b):
        operacion = a + b
        return operacion

    resultado = suma(x, y)

    # Returning the result as a JSON object
    return {
        'statusCode': 200,
        'body': json.dumps({'resultado': resultado})
    }
