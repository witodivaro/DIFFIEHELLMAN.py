import math

from random import random
from Crypto.Hash import SHA256
from lib import mod, helpers


def get_secret_key(commonSecret):
    """Creates a secret key from the calculated diffie-hellman value

    Args:
        commonSecret (bytes): Calculated value g^a^b

    Returns:
        string: Hex 16 byte key
    """    

    return SHA256.new(commonSecret).digest().hex()[:32]


def generate_public(secret, g, p):
    return mod.exp_mod(g, secret, p)


def generate_secret(g, p):
    randomValue = int(random() * 10e15)
    secret = math.floor(randomValue * p)

    return secret

def calculate_common_secret(public_key, secret, p):
    return mod.exp_mod(public_key, secret, p)