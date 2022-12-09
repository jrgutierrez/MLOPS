import requests

def get_data(gender, height):
    body_post = {
            'gender': gender,
            'height': height
    }
    result = requests.post('https://bpxcdeusfc3dt7wjjzylisdshq0umvip.lambda-url.us-east-1.on.aws/predict', json = body_post).json()
    return result