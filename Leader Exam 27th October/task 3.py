# 3) Remove Duplicates from a List (3 ქულა)
# Create a program that receives a list and removes duplicate elements while maintaining the original order.
# Examples:
# [1, 2, 2, 3, 4, 4, 5] --> [1, 2, 3, 4, 5]
# ['a', 'b', 'a', 'c'] --> ['a', 'b', 'c']

def removeDuplicates(arr):
    res = []
    for i in arr:
        if i not in res:
            res.append(i)
    return res

print(removeDuplicates([1, 2, 2, 3, 4, 4, 5]))