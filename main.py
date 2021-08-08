import os
import pandas as pd
import matplotlib.pyplot as plt
import functions.databaseOptions as dbOptions

from functions.convertNumber import convertNumber as convert

if __name__ == '__main__':
    os.system('cls')

    pd.options.display.float_format = '{:,.2f}'.format

    status = False

    while status is False:
        count_options = dbOptions.printOptions()
        option = input('Elige una opción: ')

        if option and option.isdigit():
            option = int(option)

            if option > 0 and option <= count_options: status = True
    
    dbSelect = dbOptions.optionSelect(option)
    
    status = False

    while status is False:
        code = input('Enter the code of the country you want to search for: ')

        if code:
            df = pd.read_excel('./database/' + dbSelect['route'] + '.xls', sheet_name='Data')

            if code.upper() in df['Country Code'].values:
                os.system('cls')

                status = True
                df = df[df['Country Code'] == code.upper()].reset_index()
                country = df['Country Name'].values[0]
            else: print('No country was found with this code.')
    
    data = {}
    data[country] = []
    years = [x for x in range(2010, 2021, 2)]
    
    for i in years: data[country].append(df[str(i)][0])

    result_convert = convert(data[country])
    
    for i in range(0, len(data[country])): data[country][i] /= (10**result_convert['factor'])

    data = pd.DataFrame(data=data, index=[years])
    
    fig, ax = plt.subplots()

    plt.xlabel('Years')
    plt.ylabel(result_convert['message'] + dbSelect['measure'])
    plt.title(f'{country}: ' + dbSelect['name'])

    plt.bar(years, data[country])

    if os.path.isdir('./img') is False: os.mkdir('./img')
    if os.path.isdir('./img/' + dbSelect['route']) is False: os.mkdir('./img/' + dbSelect['route'])

    plt.savefig(f'img/' + dbSelect['route'] + f'/{code.lower()}')
    plt.show()

    exit()