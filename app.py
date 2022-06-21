from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restful import Api
from config import Config

from resources.memo import MemoCreateResource
from resources.user import UserRegisterResource






app = Flask(__name__)


api = Api(app)

api.add_resource(MemoCreateResource,'/memo')
api.add_resource(UserRegisterResource, '/users/register')



if __name__ == "__main__" :
    app.run()