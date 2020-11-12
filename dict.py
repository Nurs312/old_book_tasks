users = {
    'aeinstein': {
        'first name': 'albert',
        'last name': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}
people = [users]
for names, descriptions in users.items():
    print(f'Name: {names.title()}')
    for keys, values in descriptions.items():
        print(f'{keys.title()}:{values.title()}')



