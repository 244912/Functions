# Create a function f(number, even) that computes the sum of the digits of a number.
# When the value of the even parameter is True, the function returns the sum of the even digits.
# When the value of the even parameter is False, the function returns the sum of the odd digits.
# Sample result:
# f(3124,True) returns 6
# f(3124,False) returns 4
# f(20576,False) returns 12
# f(20576,True) returns 8
# f(13115,True) returns 0

def f(number, even):
    _sum = 0
    for ch in str(number):
        digit = int(ch)
        if even and digit % 2 == 0:
            _sum += digit
        # we cant use else here because then if its even and the digit isnt even then the else will be executed
        elif not even and digit % 2 != 0:
            _sum += digit
    return _sum

print(f(3124, True))
print(f(3124, False))
print(f(20576, False))
print(f(20576, True))
print(f(13115, True))