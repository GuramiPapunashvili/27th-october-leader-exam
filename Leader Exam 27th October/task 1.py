# Create a program which receives a binary number and converts it to decimal.

# Examples:
# 10001 --> 17
# 1111 --> 15

def toBin(num):
    res = 0
    for i in str(num):
        res = res * 2 + int(i)
    return res

print(toBin(1111))
