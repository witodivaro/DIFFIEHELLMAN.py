from lib import diffiehellman, mod
import gmpy2

class Human:
    def __init__(self, name):
        self.name = name
        self.__secret = None
        self.__secret_key = None
        self.__public_key = None

    def generate_secret_key(self, g, p):
        self.__secret = diffiehellman.generate_secret(g, p)

    def generate_public_key(self, g, p):
        self.__public_key = diffiehellman.generate_public(self.__secret, g, p)

    def generate_keys(self, g, p):
        self.generate_secret_key(g, p)
        self.generate_public_key(g, p)

    def calculate_secret_key(self, public_key, p):
        if (self.__secret == None):
            raise ValueError('Own secret is not generated')

        common_secret = diffiehellman.calculate_common_secret(public_key, self.__secret, p)
        common_secret_bytes = gmpy2.to_binary(common_secret)

        self.__secret_key = diffiehellman.get_secret_key(common_secret_bytes)

    @property
    def secret_key(self):
        return self.__secret_key

    @property
    def public_key(self):
        return self.__public_key
