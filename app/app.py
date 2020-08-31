from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

class Hello(Resource):
    def get(self):
        return {"message":"This is working"}

api.add_resource(Hello,'/hello')

app.run(host='0.0.0.0',port=5000,debug=True)