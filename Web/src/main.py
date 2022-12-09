from flask import Flask, render_template, request
from resources.prediction import get_data

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
    if request.method == 'POST':
        gender = request.form.get('genderValue', 0)
        height = request.form.get('heightValue', 175)
        result = get_data(gender, height)
        actual_gender = 'selected' if int(gender) else ''
        return render_template('index.html', actual_gender = actual_gender, actual_height = height, data=str(round(result.get('weight', 75), 2)) + ' kg', pred_hid = '')
    else:
        return render_template('index.html', actual_gender = '', actual_height = 170, data='', pred_hid = 'hidden')

if __name__ == '__main__':
    app.run(debug=True, port=5001)