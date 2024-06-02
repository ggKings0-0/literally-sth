def addition(a, b):
    return a + b


def subtract(a, b):
    return a - b


def divide(a, b):
    return a / b


def multiply(a, b):
    return a * b


def raising_to_the_power(a, b):
    return a ** b


a = int(input())
sign = input()
b = int(input())

if sign == '+':
    print(addition(a, b))
if sign == '-':
    print(subtract(a, b))
if sign == '/':
    print(divide(a, b))
if sign == '*':
    print(multiply(a, b))
if sign == '**':
    print(raising_to_the_power(a, b))
