num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
match input("Choose the operation (+, -, *, /): "):
   case "+": print(f"The result is {num1 + num2}")
   case "-": print(f"The result is {num1 - num2}")
   case "*": print(f"The result is {num1 * num2}")
   case "/": print("Cannot divide by zero" if num2 == 0 else f"The result is {num1 / num2}")
   case _: print("Invalid operator")
