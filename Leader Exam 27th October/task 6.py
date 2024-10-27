# 6) Convert Pascal Case string into snake_case (4 ქულა)

# You will receive a string which will contain words in PascalCase, your job is to convert them into snake_case.

# Examples:
# "TestController"  -->  "test_controller"
# "MoviesAndBooks"  -->  "movies_and_books"
# "App7 Test"        -->  "app7_test"
# 1                 -->  "1"

def toSnake(s):
    res = []
    for i in str(s):
        if i.isalpha() and i == i.upper():
            res.append('_')
            res.append(i.lower())
        else:
            res.append(i)
    if str(s)[0].isalpha() and str(s)[0] == str(s)[0].upper():
        res.pop(0)
    while ' ' in res:
        res.remove(' ')
    return ''.join(res)

print(toSnake("App7 Test"))
