import math

from random import random
from Crypto.Hash import SHA256
from lib import mod, helpers


def get_secret_key(commonSecret):
    """Creates a secret key from the calculated diffie-hellman value

    Args:
        commonSecret (bytes): Calculated value g^a^b mod p

    Returns:
        string: Hex 16 byte key
    """    

    return SHA256.new(commonSecret).digest().hex()[:32]


def generate_public(secret, g, p):
    """Generates a public key g^secret (mod p)

    Args:
        secret (int): Secret integer in [0, 1, .., p - 1]
        g (int): Base (default is 2 by NIST)
        p (int): Prime (default is set by NIST)

    Returns:
        int: [description]
    """

    return mod.exp_mod(g, secret, p)


def generate_secret(p):
    """Generates a secret integer in [0, 1, .., p - 1]

    Args:
        p (int): Prime (default is set by NIST)

    Returns:
        int: secret integer in [0, 1, .., p - 1]
    """
    
    randomValue = int(random() * 10e15)
    secret = math.floor(randomValue * p)

    return secret

def calculate_common_secret(public_key, secret, p):
    """Calculates common secret g^a^b (mod p)

    Args:
        public_key (int): public_key, which is g^a (mod p)
        secret (int): your secret integer
        p (int): prime (usually set by NIST)

    Returns:
        int: g^a^b (mod p)
    """
    
    return mod.exp_mod(public_key, secret, p)