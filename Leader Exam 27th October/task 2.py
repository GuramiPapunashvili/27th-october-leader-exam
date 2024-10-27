# 2) Decimal --> Binary Conversion (2 ქულა)

# Create a program which receives a decimal number and converts it to binary.

# Examples:
# 17 --> 10001
# 15 --> 1111

def toDec(num):
    res = ''
    while num > 0:
        res = str(num % 2) + res
        num = num // 2
    return res

print(toDec(15))
