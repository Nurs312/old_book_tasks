animals = {
    'rex': {
        'host': 'guzman',
        'breed': 'shepherd'
    },
    'volt': {
        'host': 'carla',
        'breed': 'chihuahua'

    }
}

pets = [animals]

for pet in pets:
    for name, dict in pet.items():
        print(f'Name: {name.title()}')
        for k, v in dict.items():
            print(f'{k.title()}: {v.title()}')