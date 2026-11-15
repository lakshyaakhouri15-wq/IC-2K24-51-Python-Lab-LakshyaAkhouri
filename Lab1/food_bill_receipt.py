"""Print a sample food receipt with its item details."""

items = [
    ("Rolls", 3, 150),
    ("Burger", 2, 100),
    ("Coffee", 2, 250),
]

print("=" * 38)
print("             FOOD BILL")
print("=" * 38)
print(f"{'Food Item':<14}{'Quantity':>10}{'Price':>10}")

for item_name, quantity, price in items:
    print(f"{item_name:<14}{quantity:>10}{price:>10}")

print("-" * 38)
print(f"{'Total:':<24}{500:>14}")
print("=" * 38)
