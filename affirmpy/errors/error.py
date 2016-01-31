
class Error(RuntimeError):

    @classmethod
    def from_response(cls, response):
        return cls(
            status=response.status_code,
            code=response.code(),
            message=response.message() or response.raw_body
        )

    def __init__(self, status_code="", code="", message=""):
        self.status_code = status_code
        self.code = code
        self.message = message


    def toString(self):
        if self.code or self.message:
            return "{0} - ({1}) {2}".format(self.status_code, self.code, self.message)
        else:
            return str(self.status_code)
