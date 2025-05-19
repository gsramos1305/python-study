import art



def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

# print(operations['+'](2, 3))

def calculator():
    print(art.logo)
    should_continue = True
    num1 = float(input('First Number: '))

    while should_continue:
        for symbol in operations:
            print(symbol)
        operation_symbol = input('Pick an operation: ')
        num2 = float(input('Second Number: '))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"y to continue calculating with {answer}, n to stop: ")
        if choice == 'y':
            num1 = answer
        else:
            print("\n" * 20)
            should_continue = False
            calculator()


calculator()
