favorite_places = {
    'new york': ['nurs', 'zampu', 'abu'],
    'moscow': ['morgan', 'zampu', 'nurs'],
    'dubai': ['nurs', 'zizo', 'ratya']
}
for place, person in favorite_places.items():
    print(f'{person[0].title(), person[1].title(), person[2].title()} - they all would love to be in {place.title()}')
