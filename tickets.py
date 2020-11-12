msg = '\n\t\t\t\tWELCOME TO "<WONDERLAND>"!'
msg += '\n\t\t\t\tPlease, enter your age: '
active = True
while active:
    age = int(input(msg))
    if age < 3:
        print(" \n\t\t\t\tYou are free of charge!\n\t\t\t\tPleasant viewing!")
        break
    elif 3 <= age < 12:
        print("\n\t\t\t\tTicket costs 10$\n\t\t\t\tGo to the check out and pay for it!")
        break
    elif age >= 12:
        print("\n\t\t\t\tTicket's price is 15$ for you!\n\t\t\t\tWonderful viewing!")
        break
