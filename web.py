from flask import Flask, request, jsonify
import json
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)

class status(Resource):
    def get(self):
        js = {
           "status": "OK"
        }
        return jsonify(js)

api.add_resource(status, '/')

class statusDocker(Resource):
    def get(self):
        js = {
           "status": "OK"
        }
        return jsonify(js)

api.add_resource(statusDocker, '/status')

if __name__ == "__main__":
	app.run(debug=True, use_reloader=True)











