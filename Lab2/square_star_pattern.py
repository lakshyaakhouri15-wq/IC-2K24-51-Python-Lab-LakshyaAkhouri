"""Draw a square whose sides are made of star characters."""

side_length = int(input("Enter the square size: "))

for _ in range(side_length):
    print("* " * side_length)
