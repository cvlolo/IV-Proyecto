from flask import Flask, request, jsonify
import json
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)


@app.route("/")
def bienvenido():
    data = {"status": "OK"}
    return json.dumps(data)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)

