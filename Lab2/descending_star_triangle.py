"""Print an inverted, left-aligned triangle of stars."""

height = int(input("Enter the number of rows: "))

for row_number in range(height, 0, -1):
    print("* " * row_number)
