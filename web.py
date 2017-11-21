from flask import Flask,request, jsonify
import os
import json

app = Flask(__name__)


{
   "status": "OK"
}



@app.route("/")
def rutaStatus():
    return jsonify(status='OK')

@app.route("/status")
def rutaStatusDocker():
    return jsonify(status='OK')

if __name__ == "__main__":
	app.run(debug = True, use_reloader = True)


