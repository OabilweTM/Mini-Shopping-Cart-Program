#Exercise 2 - Shopping Cart program

item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))           #>> typecasting used
quantity = int(input("How many would you like?: "))    #>> typecasting used
total = price * quantity

print(f"You have bought {quantity} x {item}/s")
print(f"Your total is R{total} ")