"""Collect a few personal details and display them."""

person_name = input("Enter your name: ").strip()
person_age = input("Enter your age: ").strip()
person_city = input("Enter your city: ").strip()

print(
    f"My name is {person_name}, I am {person_age} years old, "
    f"and I live in {person_city}."
)
