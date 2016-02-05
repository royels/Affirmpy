from affirmpy.client import Client
from affirmpy.static import AffirmStatic


class API(object):
    public_key = None
    secret_key = None
    api_url = "https://sandbox.affirm.com/api/v2/"

    @classmethod
    def client(cls):
        return Client(
            public_key= cls.public_key,
            secret_key= cls.secret_key,
            api_url = cls.api_url
        )
