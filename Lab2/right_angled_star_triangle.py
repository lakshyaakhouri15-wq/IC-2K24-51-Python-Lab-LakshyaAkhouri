"""Print a left-aligned right-angled triangle of stars."""

height = int(input("Enter the triangle height: "))

for row_number in range(1, height + 1):
    print("* " * row_number)
