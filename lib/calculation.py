import math


def add(first_number: int | float, second_number: int | float) -> int | float:
    return first_number + second_number


def subtract(first_number: int | float, second_number: int | float) -> int | float:
    return first_number - second_number


def multiply(first_number: int | float, second_number: int | float) -> int | float:
    return first_number * second_number


def divide(first_number: int | float, second_number: int | float) -> int | float | None:
    try:
        if type(first_number) == float or type(second_number) == float:
            return first_number / second_number
        return first_number // second_number
    except ZeroDivisionError:
        return None


def logarithm(first_number: int | float, second_number: int | float) -> int | float | None:
    try:
        return math.log(first_number, second_number)
    except ZeroDivisionError:
        return None


def power(first_number: int | float, second_number: int | float) -> int | float:
    return first_number ** second_number


def square_root(first_number: int | float) -> int | float | None:
    return first_number ** .5


def cube_root(first_number: int | float) -> int | float | None:
    return math.cbrt(first_number)


def factorial(first_number: int | float) -> int | float | None:
    if first_number < 2:
        return 1
    return first_number * factorial(first_number - 1)
