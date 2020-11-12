favorite_numbers = {
    'nurs': [1, 2],
    'abu': [3, 4],
    'sima': [5, 6]
}

for person, numbers in favorite_numbers.items():
    if person == 'nurs':
        print(f"{person.title()}' favorite numbers are: {numbers}")

    else:
        print(f"{person.title()}'s favorite numbers are: {numbers}")
