"""Read two integers and display their basic arithmetic results."""

first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

addition = first_number + second_number
subtraction = first_number - second_number
multiplication = first_number * second_number

print(f"Sum: {addition}")
print(f"Difference: {subtraction}")
print(f"Product: {multiplication}")

if second_number != 0:
    print(f"Quotient: {first_number / second_number}")
    print(f"Remainder: {first_number % second_number}")
else:
    print("Quotient: cannot divide by zero")
    print("Remainder: cannot divide by zero")
