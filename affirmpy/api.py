from affirmpy.client import Client
from affirmpy.static import Static


class API(object):
    public_key = Static.public_key
    secret_key = Static.secret_key
    api_url = Static.api_url

    @classmethod
    def client(cls):
        return Client(
            public_key= cls.public_key,
            secret_key= cls.secret_key,
            api_url = cls.api_url
        )



