import math

def convertNumber(data):
    result = {
        'factor': 0,
        'message': '',
    }

    max_value = max(data)
    count_digits = len(str(math.ceil(max_value)))

    if count_digits > 3:
        result['factor'] = math.floor((count_digits - 1) / 3) * 3
    
    if result['factor'] == 1: result['message'] = 'Thousands '
    elif result['factor'] == 2: result['message'] = 'Million '
    elif result['factor'] > 2: result['message'] = 'Billion '

    return result