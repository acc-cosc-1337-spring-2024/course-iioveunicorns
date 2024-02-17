#

def get_factorial(num):
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    return factorial

def sum_odd_numbers(num):
    sum = 0
    while num >= 1:
        if num % 2 == 1:
            sum +=num 
            num -= 1
        else:
            num -= 1
    return sum