from math import *


# --------------------------------
# This function is just able to take relative number, no float, no double
# @param value : is the value that you want to convert in binary code
# @param octet : is how many octet do you want to represent your value
# @param signed : insert true if your value is negative and false if your value is positive
# --------------------------------

def encodeToBinary(value, octet, signed):
    value = abs(value)
    binary = []  # List of your octet composed of 8 bits
    rest = value  # Local variable used for decomposition in power of two
    power = 0
    while valueR > maxNumberOctets(octet, signed):
        octet += 1

    for i in range(octet):
        binary.insert(i, [0, 0, 0, 0, 0, 0, 0, 0])

    while rest != 0:
        if rest >= 2 ** power:
            power += 1
        else:
            if power != 0:
                power -= 1
            rest -= 2 ** power
            localOctet = binary[power//8]
            localOctet[7 - power] = 1
            power = 0


def maxNumberOctets(octet, signed):
    number = 0
    signed_value = 0
    if signed:
        signed_value = 1
    for i in range(octet * 8 - signed_value):
        number += 2 ** i
    return number


encodeToBinary(46, 1, False)
