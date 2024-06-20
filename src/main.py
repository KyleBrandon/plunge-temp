from temp import read_temp
import datetime
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    temp_f = read_temp()
    return jsonify(message=temp_f)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
