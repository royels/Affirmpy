import json

class Response(object):

    def __init__(self, success, status_code, body):
        self.raw_body = body
        self.success = success
        self.status_code = int(status_code)

    def is_success(self):
        return self.success

    def is_error(self):
        return not self.is_success()

    def body(self):
        try:
            return json.load(self.raw_body)
        except Exception:
            return {}


    def type(self):
        return self.body()['type']

    def code(self):
        return self.body()['code']

    def message(self):
        return self.body()['message']

    def field(self):
        return self.body()['field']

