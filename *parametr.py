def make_pizza(size, *toppings):
    print(f'\nWe are making a pizza with following toppings:\nSize of the pizza is {size}')
    for topping in toppings:
        print(f'\t---> {topping}')


make_pizza(50, 'xui', 'dermo', 'govno')
