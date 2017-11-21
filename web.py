from flask import Flask,request, jsonify
import os
import json

app = Flask(__name__)


{
   "status": "OK"
}



@app.route("/")
def principal():
    data = {"status": "OK"}
    return jsonify(data)

@app.route("/status")
def docker():
    data = {"status": "OK"}
    return jsonify(data)

if __name__ == "__main__":
	app.run(debug = True, use_reloader = True)


