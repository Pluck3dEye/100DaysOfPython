from art import logo


def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    return a / b


operator = {
    "+": addition,
    "-": subtraction,
    "*": multiplication,
    "/": division
}

print(logo)
end_program = False

while not end_program:
    end_multiple_times = False
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operation = input("Enter the operation: ")
    while operation not in operator.keys():
        print("Invalid")
        operation = input("Enter the operation: ")
    result = operator[operation](num1, num2)
    print(result)
    while not end_multiple_times:
        if input(f"Do you want to continue with {result} ? (y/n): ").lower() == "y":
            num1 = result
            num2 = float(input("Enter second number: "))
            operation = input("Enter the operation: ")
            while operation not in operator.keys():
                print("Invalid input")
                operation = input("Enter the operation: ")
            result = operator[operation](num1, num2)
        else:
            end_multiple_times = True

    if input("Do you want to continue with another calculation? (y/n): ") == "n":
        end_program = True


