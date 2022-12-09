import joblib
from pathlib import Path

__version__ = '0.1.0'

BASE_DIR = Path(__file__).resolve(strict = True).parent

#with open(f'{BASE_DIR}/model.pkl', 'rb') as f:
#    model = pickle.load(f)
#
#with open(f'{BASE_DIR}/preprocessor.pkl', 'rb') as f:
#    preprocessor = pickle.load(f)

preprocessor = joblib.load(f'{BASE_DIR}/preprocessor.joblib')
model = joblib.load(f'{BASE_DIR}/model.joblib')

def prediction(gender, height):
    data = [[gender, height]]
    data = preprocessor.transform(data)
    pred = model.predict(data, verbose = 0)
    return pred[0][0]