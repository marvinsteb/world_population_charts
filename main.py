import utils
import read_csv
import charts
import pandas as pd


def run():
    data = read_csv.read_csv('./data.csv')

    country = 'Guatemala'
    dict_by_country = utils.dict_by_country(data, country)
    if bool(dict_by_country):
        labes, values = utils.population_by_contry(dict_by_country[0])
        charts.generate_bar_chart(country, labes, values)
        
    continent = "Africa"
    
    data_frame = pd.read_csv('./data.csv')
    data_frame  = data_frame[data_frame['Continent'] == continent]
    countries = data_frame['Country/Territory'].values
    percentages = data_frame['World Population Percentage']
    charts.generate_pie_chart(continent,countries, percentages)
    
    '''
    data = utils.population_by_continent(data, continent)
    if bool(data):
        labels, values = utils.world_population(data)
        charts.generate_pie_chart(labels, values)
    '''


if __name__ == "__main__":
    run()
