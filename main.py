from flask import Flask
import pandas as pd

df = pd.read_csv('./data/utilization2019.csv')

app = Flask(__name__)

@app.route('/', methods = ["GET"])
def home():
    return "This is an API service for MN ICD Code details"


@app.route('/preview', methods = ["GET"])

def preview():
    top10rows = df.head(1)
    result = top10rows.to_json(orient="records")
    return result

if __name__ == '__main__':
    app.run(debug=True)  