num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))
operation = input("Choose the operation (+, -, *, /):")
result = 0

match operation:
    case "+":
        result = num1 + num2
    case "-":
        result = num1 - num2
    case "*":
        result = num1 * num2
    case "/":
        result = "Cannot divide by zero" if num1 == 0 or num2 == 0 else num1/num2
    case _:
        result = "Operation not included"

print("The result is {}.".format(result) if type(result) is float else result)

