# function for basic arithmatic operators of two integers or decimals
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y != 0:
        return x/y
    else:
        return "CANNOT DIVIDE"


# taking user input from user before proceeding to choice of arithmatic operations
def user_input():
    global num1
    num1 = float(input("num1 -> "))
    global num2
    num2 = float(input("num2 -> "))


ch = 1

user_input()

# while loop for arithmatic operations
while ch > 0:
    print("1. Addition")
    print("2. Subtractions")
    print("3. Multiplication")
    print("4. Division")
    print("5. Reset")
    print("6. Exit")
    ch = int(input("Enter your choice -> "))

    if ch == 1:
        print("Result -> ", add(num1, num2))

    elif ch == 2:
        print("Result -> ", subtract(num1, num2))

    elif ch == 3:
        print("Result -> ", multiply(num1, num2))

    elif ch == 4:
        print("Result -> ", divide(num1, num2))

    elif ch == 5:
        user_input()

    elif ch == 6:
        ch = 0
   