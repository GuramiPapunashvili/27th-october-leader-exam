# 5) Palindrome Checker (3 ქულა)
# Create a program that checks if a given string is a palindrome (reads the same forward and backward). The function should ignore spaces, punctuation, and capitalization.
# Examples:
# "A man a plan a canal Panama" --> True
# "Hello" --> False

def palindromeCheck(str):
    arr = [i for i in str]
    for i in range(len(arr)):
        if arr[i].isalpha() == False:
            arr.remove[arr[i]]
    joined = ''.join(arr)
    if joined.lower() == joined[::-1].lower():
        return True
    return False

print(palindromeCheck("racecar,"))