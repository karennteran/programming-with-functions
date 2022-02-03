from datetime import date
# from datetime import datetime

# current_day = datetime.now()
# weekday = current_day.weekday()

today = date.today().strftime("%A")
sales_tax = 0.06


# subtotal = float(input("Enter the subtotal: "))

# strentch challenge
cost = 1
subtotal = 0
while cost != 0:
    cost = float(input("what is the price of the item? "))
    if cost > 0:
        quantity = int(input("how many are you buying? "))
        price = cost * quantity
        subtotal += price


if subtotal >= 50 and (today.lower() == "tuesday" or today.lower() == "wednesday"):
    discount = 0.10
    discount_amount = subtotal * discount
    # print(discount_amount)
    subtotal = subtotal - discount_amount
    # print(subtotal)
    tax = subtotal * sales_tax
    total = subtotal + tax
    # print(total)
else:
    tax = subtotal * sales_tax
    total = subtotal + tax
    # print(total)

# strenght challenge
if subtotal < 50 and (today.lower() == "tuesday" or today.lower() == "wednesday"):
    missing = 50 - subtotal
    print(f"you are ${missing:.2f} short of being elegible for the discount")

print(f"sales tax: ${tax:.2f}")
print(f"your total is: ${total:.2f}")


