num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
op = input("Choose the operation (+, -, *, /): ")

match op:
    case '+':
        print("The result is ", num1 + num2)

    case '-':
        print("The result is ", num1 - num2)
    case '*':
        print("The result is ", num1 * num2)
    case '/':
        if num2 != 0:
            print("The result is ", num1 / num2)
        else:
            print("You can not divide by zero!")
    case _: 
        print("Invalid operator!")
