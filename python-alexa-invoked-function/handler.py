def hello(event, context):
    response = {
        'version': '1.0',
        'response': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': 'Hello World!'
            }
        }
    }

    return response
