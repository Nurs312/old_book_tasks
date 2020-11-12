unconfirmed_users = ['Nurs', 'Zampu', 'Morgan']
confimed_users = []
while unconfirmed_users:
    losers = unconfirmed_users.pop()
    confimed_users.append(losers)
    print(f"\t\t\t\tVerifying users: {losers.title()}")
print(f'\n\t\tThese users just have been confirmed: ')
for confimed_user in confimed_users:
    print("\t\t\t\t"+confimed_user.title())
