options = [
    { 'name': 'PIB', 'route': 'pib', 'measure': 'USD' },
    { 'name': 'Total Population', 'route': 'pob_total', 'measure': 'People' },
    { 'name': 'Life expectancy at birth', 'route': 'life_expectancy_at_birth', 'measure': 'Years' },
    { 'name': 'School Enrollment, Primary Level', 'route': 'primary_level', 'measure': 'Percentage' },
]

def printOptions():
    counter = 1

    for option in options:
        print(f'[{counter}] ' + option['name'])
        counter += 1
    
    return len(options)

def optionSelect(number): return options[number - 1]