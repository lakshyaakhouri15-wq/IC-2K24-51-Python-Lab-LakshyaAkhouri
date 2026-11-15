"""Display a centered triangle made from star characters."""

height = int(input("How many rows should the triangle have? "))

for row_number in range(1, height + 1):
    indentation = " " * (height - row_number)
    stars = "* " * row_number
    print(indentation + stars)
