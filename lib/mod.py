import gmpy2 as math
from lib import helpers


def mul_mod(a, b, modulus):
    # (A * B) mod C = ((A mod C) * (B mod C)) mod C
    intermediateMultiplication = (
        math.f_mod(a, modulus)
        * math.f_mod(b, modulus)
    )

    return math.f_mod(intermediateMultiplication, modulus)


def add_mod(a, b, modulus):
    aMod = a if a < modulus else a % modulus
    bMod = b if b < modulus else b % modulus

    # (A + B) mod C = (A mod C + B mod C) mod C
    intermediateAddition = (aMod * bMod)

    return math.f_mod(intermediateAddition, modulus)


def exp_mod(base, power, modulus):
    power_binary = helpers.convertToBinary(power)

    result = 1

    for i in range(0, len(power_binary)):
        bit = power_binary[i]

        if (bit == '1'):
            result = mul_mod(result, base, modulus)

        if (i != len(power_binary) - 1):
            result = mul_mod(result, result, modulus)

    return result
