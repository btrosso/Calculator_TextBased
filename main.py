

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

num1 = int(input("What's the first number?: "))
for symbol in operations:
    print(symbol)
op_symbol = input("Pick and operation from the line above: ")
num2 = int(input("What's the second number?: "))

calculation = operations[op_symbol]
answer = calculation(num1, num2)

print(f"{num1} {op_symbol} {num2} = {answer}")

