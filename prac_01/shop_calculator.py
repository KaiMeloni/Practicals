"""
The program allows the user to enter the number of items and the price of each different item.
Then the program computes and displays the total price of those items.
If the total price is over $100, then a 10% discount is applied to that total before the amount is displayed on the
screen

"""

total_sale = 0
items = int(input("Number of items: "))
while items < 0:
    print("Invalid amount")
    items = int(input("Number of items: "))
for i in range(items):
    price = float(input("Price of items: "))
    total_sale += price

if total_sale > 100:
    total_sale *= 0.9

print("The total price of the items is: $", total_sale)

# Could use print("Total price for {} items is ${:.2f}".format(item, total_sale))
