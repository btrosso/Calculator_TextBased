from art import logo


# Add
def add(n1, n2):
    return n1 + n2


# Subtract
def subtract(n1, n2):
    return n1 - n2


# Multiply
def multiply(n1, n2):
    return n1 * n2


# Divide
def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    print(logo)

    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    answer = num1

    keep_going = 'y'
    while keep_going == 'y':
        temp = answer
        op_symbol = input("Pick an operation: ")
        new_num = float(input("What's the next number?: "))
        calculation = operations[op_symbol]
        answer = calculation(temp, new_num)
        print(f"{temp} {op_symbol} {new_num} = {answer}")
        keep_going = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to begin a new calculation. ")

        if keep_going == 'n':
            calculator()


calculator()