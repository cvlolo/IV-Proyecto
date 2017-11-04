from flask import Flask, request, jsonify
import json
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)


class Status(Resource):
    def status(self):

        schema = {
           "status": "OK"
        }

        return jsonify(schema)

api.add_resource(checkStatus, '/')

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)

