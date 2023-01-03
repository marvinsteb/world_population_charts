import utils
import read_csv
import charts


def run():
    data = read_csv.read_csv('./data.csv')

    country = 'Guatemala'
    dict_by_country = utils.dict_by_country(data, country)
    if bool(dict_by_country):
        labes, values = utils.population_by_contry(dict_by_country[0])
        charts.generate_bar_chart(country, labes, values)

    continent = "South Americaas"
    data = utils.population_by_continent(data, continent)
    if bool(data):
        labels, values = utils.world_population(data)
        charts.generate_pie_chart(labels, values)


if __name__ == "__main__":
    run()
