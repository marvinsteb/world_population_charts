import re


def dict_by_country(data, country):
    result = list(
        filter(lambda item: item['Country/Territory'] == country, data))
    return result[0]


def population_by_contry(data):
    population_dict = {k.split(' ')[0]: int(v) for (k, v) in data.items() if bool(
        re.match(r'^([1-3][0-9]{3})', k))}

    return population_dict.keys(), population_dict.values()
