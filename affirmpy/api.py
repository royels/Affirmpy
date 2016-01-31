from affirmpy.client import Client
from affirmpy.static import AffirmStatic


class API(object):
    public_key = AffirmStatic.public_key
    secret_key = AffirmStatic.secret_key
    api_url = AffirmStatic.api_url

    @classmethod
    def client(cls):
        return Client(
            public_key= cls.public_key,
            secret_key= cls.secret_key,
            api_url = cls.api_url
        )



