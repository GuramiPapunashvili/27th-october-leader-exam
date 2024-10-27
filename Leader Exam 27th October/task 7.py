# 7) Fibonacci Sequence Generator (4 ქულა)
# Create a program that receives an integer n and returns the first n numbers in the Fibonacci sequence. The sequence starts with 0 and 1, and each subsequent number is the sum of the previous two.
# Examples:
# 5 --> [0, 1, 1, 2, 3]
# 7 --> [0, 1, 1, 2, 3, 5, 8]

def nth_in_fibonacci(num):
    fibo_nums = [0,1]
    for i in range(num+1):
        fibo_nums.append(sum(fibo_nums[i:i+2]))
    return fibo_nums[:num]

print(nth_in_fibonacci(7))
    