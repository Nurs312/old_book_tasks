cities = {
    'new york': {
        'country': 'usa',
        'populaion': '8 405 837',
        'fact': 'ахуенный'
    },
    'moscow': {
        'country': 'russia',
        'population': '12 678 079',
        'fact': 'пиздатый'
    },
    'istanbul': {
        'country': 'turkey',
        'population': '15 029 231',
        'fact': 'душевный'
    }
}
for city, info in cities.items():
    print(f'City: {city.title()}')
    for k, v in info.items():
        print(f'{k.title()}: {v.title()}')
