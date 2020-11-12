responses = {}
active = True
while active:
    name = input("\nWhat is your name?: ")
    response = input("\nWhich mountain would you like to climb someday?: ")
    responses[name] = response
    check = input("Would you like to let another person respond? (y/n) ").lower()
    if check == 'no':
        active = False
        print("\n---Poll Result---")
        for name, response in responses.items():
            print(f'{name.title()} would like to climb {response.title()}')
