from math import *


# --------------------------------
# This function is just able to take natural number, no float, no double
# @param value : is the value that you want to convert in binary code
# @param octet : is how many octet do you want to represent your value
# --------------------------------

def encodeToBinary(value, octet):
    value = abs(value)
    binary = []  # List of your octet composed of 8 bits
    rest = value  # Local variable used for decomposition in power of two
    power = 0
    while value > maxNumberOctets(octet):
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
            localOctet = binary[power // 8]
            localOctet[power%8] = 1
            power = 0
    binary.reverse() 
    for octet in binary:
        octet.reverse()
    return binary


# --------------------------------
# @param binary is the list of octet and bit
# --------------------------------

def decodeToNumber(binary):
    number = 0
    power_position = 0
    binary.reverse()
    for i in binary:
        local_octet = i
        local_octet.reverse()
        for i in local_octet :
            if i == 1:
                number+=(2**power_position)
            power_position+=1   
        local_octet.reverse()
    binary.reverse()  
    return number

def maxNumberOctets(octet):
    number = 0
    signed_value = 0
    for i in range(octet * 8 - signed_value):
        number += 2 ** i
    return number


encoded = encodeToBinary(2**100, 1)
decoded = decodeToNumber(encoded)
print(encoded)
print(decoded)
