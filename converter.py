def convert_length(value, from_unit, to_unit):
    units = {
        'm': 1,
        'km': 1000,
        'cm': 0.01,
        'mm': 0.001,
    }

    if from_unit not in units or to_unit not in units:
        return "Invalid units"

    if from_unit == 'km' and to_unit == 'm':
        return value * 1000
    elif from_unit == 'm' and to_unit == 'km':
        return value / 1000
    elif from_unit == 'cm' and to_unit == 'm':
        return value * 0.01
    elif from_unit == 'm' and to_unit == 'cm':
        return value * 100
    elif from_unit == 'mm' and to_unit == 'm':
        return value * 0.001
    elif from_unit == 'm' and to_unit == 'mm':
        return value * 1000
    else:
        return "Invalid units"


def convert_weight(value, from_unit, to_unit):
    units = {
        'g': 1,
        'kg': 1000,
        'ton': 1000000,
    }

    if from_unit not in units or to_unit not in units:
        return "Invalid units"

    return value * (units[to_unit] / units[from_unit])


def convert_temperature(value, from_unit, to_unit):
    if from_unit == 'C':
        if to_unit == 'F':
            return (value * 9 / 5) + 32
        elif to_unit == 'K':
            return value + 273.15
        else:
            return value

    elif from_unit == 'F':
        if to_unit == 'C':
            return (value - 32) * 5 / 9
        elif to_unit == 'K':
            return (value - 32) * 5 / 9 + 273.15
        else:
            return value

    elif from_unit == 'K':
        if to_unit == 'C':
            return value - 273.15
        elif to_unit == 'F':
            return (value - 273.15) * 9 / 5 + 32
        else:
            return value
    else:
        return "Invalid units"


def convert_currency(value, from_unit, to_unit):
    if from_unit == 'USD' and to_unit == 'VND':
        return value * 24000
    elif from_unit == 'VND' and to_unit == 'USD':
        return value / 24000
    else:
        return "Invalid currency units"