# 9) Prime time (4 ქულა)

# Write a function that takes a maximum bound and returns all primes up to and including the maximum bound.

# For example:
# 11 => [2, 3, 5, 7, 11]

def primes(num):
    res = []
    for i in range(2,num+1):
        count = 0
        for x in range(1,num+1):
            if i % x == 0:
                count += 1
            else:
                continue
        if count == 2:
            res.append(i)
    return res

print(primes(11))