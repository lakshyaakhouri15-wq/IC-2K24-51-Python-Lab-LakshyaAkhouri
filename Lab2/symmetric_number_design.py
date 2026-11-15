"""Display the symmetric number pattern using nested loops."""

pattern_size = int(input("Enter the pattern size: "))

for row_index in range(1, 2 * pattern_size):
    mirrored_row = (
        row_index if row_index <= pattern_size
        else 2 * pattern_size - row_index
    )

    for column_index in range(1, 2 * pattern_size):
        mirrored_column = (
            column_index if column_index <= pattern_size
            else 2 * pattern_size - column_index
        )

        nearest_edge = min(mirrored_row, mirrored_column)
        print(pattern_size - nearest_edge + 1, end=" ")

    print()
