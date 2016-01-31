import requests
import json
import os

class Client(object):
	def __init__(self, public_key, secret_key, api_url):
		self.public_key = public_key
		self.secret_key = secret_key
		self.api_url = api_url

	def post(self, path, data={}):
		self.make_request(path, self.post.__name__, data )

	def get(self, path, data={}):
		self.make_request(path, self.get.__name__, data )

	def make_request(self, path, method, data):
		response = requests.request(
			method=method,
			url=self.url(path),
			data=json.dumps(data),
			headers=self.affirm_headers(data),
			auth=(self.public_key, self.secret_key)
		)
		affirmed_response = affirmify(response)
		handle_error(affirmed_response)

	def affirmify(self, response):



	def _url(self, path):
		return os.path.join(self.api_url, path)


	def _affirm_headers(self, data):
		if len(data):
			return { "Content-Type" : "application/json"}
