from flask import Flask, request, jsonify
import json
from flask_restful import Resource, Api


app = Flask(__name__)

{
   "status": "OK"
}

@app.route("/")
def func():
    data = {"status": "OK"}
    return json.dumps(data)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug = True, use_reloader = True)
