"""Demonstrate common string methods and the len function."""

user_name = input("Enter your name: ")

clean_name = user_name.strip()

print(f"Uppercase: {clean_name.upper()}")
print(f"Lowercase: {clean_name.lower()}")
print(f"Without extra spaces: {clean_name}")
print(f"Length: {len(clean_name)}")
