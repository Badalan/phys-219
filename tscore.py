# !python3
import sys
import math

# A = float(sys.argv[1])
# B = float(sys.argv[2])
# dA = float(sys.argv[3])
# dB = float(sys.argv[4])


def tscore(A, B, dA, dB):
    return (math.fabs(A - B)/math.sqrt(dA**2 + dB**2))

# print(tscore(A, B, dA, dB))
