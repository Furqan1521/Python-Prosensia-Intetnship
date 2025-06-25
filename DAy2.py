full_name = input("Enter your full name")

first_name, last_name = full_name.split()

print(f"First Name: {first_name}")
print(f"Last Name: {last_name}")

number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

print(f"{number1} + {number2} = {number1 + number2}")
print(f"{number1} - {number2} = {number1 - number2}")
print(f"{number1} * {number2} = {number1 * number2}")
print(f"{number1} / {number2} = {number1 / number2}" if number2 != 0 else "Division by zero is not allowed.")
