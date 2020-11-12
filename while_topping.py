promt = "\nChoose tooppings you want to add to your pizza"
promt += "\nEnter 'quit' when you are finish "
while True:
    topping = input(promt).lower()
    if topping == 'quit':
        break
    else:
        print(f"\n\tWe added >>>{topping.title()}<<< to your pizza!")