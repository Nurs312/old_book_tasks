vocation = {}
active = True
while active:
    msg = input('\nWhat is your name?: ')
    msg1 = input('\n Where would you like to go for a holiday?: ')
    vocation[msg] = msg1
    checkpoint = input("Do you want to continue the poll? (y/n): ").lower()
    if checkpoint == 'no':
        active = False
    print(f'{msg.title()} would love to rest in {msg1.title()}')