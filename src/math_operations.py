import math


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def modulus(a, b):
    return a % b


def power(a, b):
    return a ** b

def absolute(a):
    return abs(a)

def square(a):
    return a ** 2

def sqrt(a):
    return math.sqrt(a)