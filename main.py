import lib

welcome_text = """
========= Fuzi Calculator app =========
Hi there! Welcome to my calculator app."""

print(welcome_text)

choices = """
Please choose the unit you want to go to:
C for calculator.
S for settings.
Your choice: """

unit = input(choices)


def get_first_number() -> int | float | None:
    """ Get first number from input and return it as int type if is number, else print invalid number error and
     return None """
    try:
        first_number = float(input("Number: "))
        return first_number if not first_number.is_integer() else int(first_number)
    except ValueError:
        print("Invalid number")
        return None


def get_second_number() -> int | float | None:
    """" Get second number from input and return it as int type if is number, else print invalid number error and
    return None """
    try:
        second_number = float(input("Number: "))
        return second_number if not second_number.is_integer() else int(second_number)
    except ValueError:
        print("Invalid number")
        return None


def get_operator() -> str | None:
    """" Get operator from input and return it if entered, else return None """
    operators_text = """
    Please enter the operator.
    Valid operators are:
    + for addition.
    - for minus.
    * for multiplication.
    / for dividing.
    // for square root.
    /// for cube root.
    log for logarithm.
    ** for power.
    ! for factorial.
    Your choice: """
    operator = input(operators_text)
    return operator if operator != "" else None


def calculator() -> int | float | None:
    """" Calculate the first and second number based on operator and return the result as number, else return
    None"""
    print("=== CALCULATOR ===")
    first_number = get_first_number()
    if first_number is not None:
        operator = get_operator()
        if operator is not None:
            operators = [
                "*",
                "**",
                "/",
                "+",
                "-",
                "log",
            ]
            if operator in operators:
                second_number = get_second_number()
                if second_number is not None:
                    return {
                        "+": lib.add,
                        "-": lib.subtract,
                        "*": lib.multiply,
                        "/": lib.divide,
                        "l": lib.logarithm,
                        "**": lib.power,
                    }.get(operator, lib.add)(first_number, second_number)
                return None
            return {
                "//": lib.square_root,
                "///": lib.cube_root,
                "!": lib.factorial,
            }.get(operator, lib.square_root)(first_number)
        return None
    return None


def settings():
    """ TODO: Add settings feature in future :) """
    pass


if unit.lower().startswith("c"):
    """ Call the calculator function if the given input 
    starts with c letter """
    print(calculator())
    while True:
        answer = input(" Do you want to repeat?(y/n): ")
        if answer.lower() .startswith("y"):
            print(calculator())
        elif answer.lower().startswith("n"):
            break
        else:
            continue


elif unit.lower().startswith("s"):
    """ Call the settings function if the given input 
    starts with s letter """
    settings()

else:
    pass
