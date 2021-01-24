from math import *

height = 10.0
distance = 10.0

n1 = 1.0
n2 = 1.2


def getLength(distance_two):
    l1 = sqrt(height ** 2 + distance_two ** 2)
    l2 = sqrt((distance - distance_two) ** 2 + height ** 2)
    optical_path = l1 * n1 + l2 * n2
    return optical_path


length_min = 10.0 ** 9
dist_best = 0

for i in range(0, 10000):
    dist = i * (distance / 10000)
    length = getLength(dist)
    if length_min > length:
        length_min = length
        dist_best = dist


sinI1 = dist_best/sqrt(dist_best**2+height**2)
sinI2 = (distance-dist_best)/sqrt((distance-dist_best)**2+height**2)

print(sinI1)
print(sinI2*n2)

