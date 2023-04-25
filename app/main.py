import utils
import read_csv
import charts
import pandas as pd

def run():
  '''
  data = list(filter(lambda item : item['Continent'] == 'South America',data))
  countries = list(map(lambda x: x['Country/Territory'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  '''

  df = pd.read_csv('data.csv')
  df = df[df['Continent'] == 'Africa']
  country = input('Type Country => ')

  countries = df['Country/Territory'].values
  percentages = df['World Population Percentage']
  charts.generate_pie_chart(country, countries, percentages)

  data = read_csv.read_csv('./data.csv')
  print(country)

  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(country['Country/Territory'], labels, values)


if __name__ == '__main__':
  run()