"""Print a rhombus pattern using a fixed number of stars per row."""

height = int(input("Enter the rhombus height: "))

for row_index in range(height):
    leading_spaces = " " * (height - row_index - 1)
    star_sequence = "* " * height
    print(leading_spaces + star_sequence)
