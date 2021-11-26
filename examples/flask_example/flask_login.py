from flask import Flask, request
from flask_restful import Api, Resource
import os
from ascrypt import AScrypt
from ascrypt import exceptions as asce

app = Flask(__name__, template_folder=os.getcwd())
api = Api(app)

ascrypt_key = AScrypt.generate_key(len=64)

class Home(Resource):
	def get():
		token = request.headers.get('auth')

		if not token:
			response = {'status': 'error', 'message': 'Você precisa estar autenticado para acessar'}

		# validando token
		try:
			content = AScrypt(ascrypt_key).decode_token(token)
		except (asce.InvalidTypeToken, asce.InvalidToken) as err:
			# token inválido
			print(err)
			response = {'status': 'error', 'message': 'Faça login para proseguir'}
		else:
			response = content

		return response

class Auth(Resource):
	def post():
		# create login
		info_user = request.json

		token = AScrypt(ascrypt_key).new_token(info_user)
		return {'status': 'sucess', 'token': token}


api.add_resource(Auth, '/login')
api.add_resource(Home, '/')