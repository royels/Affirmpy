import requests
import json
import os

from .response import Response


class Client(object):
    def __init__(self, public_key, secret_key, api_url):
        self.public_key = public_key
        self.secret_key = secret_key
        self.api_url = api_url

    def post(self, path, data={}):
        self.make_request(path, self.post.__name__, data)

    def get(self, path, data={}):
        self.make_request(path, self.get.__name__, data)

    def make_request(self, path, method, data):
        response = requests.request(
            method=method,
            url=self._url(path),
            data=json.dumps(data),
            headers=self._affirm_headers(data),
            auth=(self.public_key, self.secret_key)
        )
        affirmed_response = self._affirmify(response)
        self._handle_error(affirmed_response)

    def _affirmify(self, response):
        return Response(
            success=(response.status_code == requests.codes.ok),
            status_code=response.status_code,
            body=response.json
        )

    def _handle_error(self, affirmed):
        if affirmed.status_code == 401:
            self._raise_error(error.AuthenticationError, affirmed)
        elif affirmed.status_code == 404:
            self._raise_error(error.ResourceNotFoundError, affirmed)
        elif affirmed.status_code >= 500:
            self._raise_error(error.ServerError, affirmed)
        else:
            pass

        return affirmed

    def _raise_error(self, error, affirmed):
        raise error.from_response(affirmed)

    def _url(self, path):
        return os.path.join(self.api_url, path)

    def _affirm_headers(self, data):
        if len(data):
            return {"Content-Type": "application/json"}
