# import csv
#
# with open('weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for index, row in enumerate(data):
#         if index != 0:
#             temperatures.append(int(row[1]))
#
#     print(temperatures)

import pandas

# data = pandas.read_csv('weather_data.csv')
# temp_data = data['temp'].to_list()

# avg_temp = sum(temp_data) / len(temp_data)
# print(round(avg_temp))

# print(temp_data)
# print(data['temp'].mean())
# print(data['temp'].max())

# print(data[data.temp == data['temp'].max()])

# monday_temp_celsius = data[data.day == 'Monday'].temp
# monday_temp_fahrenheit = (monday_temp_celsius * 1.8) + 32
# print(monday_temp_fahrenheit)

# data_dict = {
#     'students': ["Bob", 'Mob', "Pop"],
#     'scores': [100, 50, 25]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv('new_data.csv')
# print(data)

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
groups = data.groupby(pandas.Grouper(key='Primary Fur Color')).size()

df = pandas.DataFrame(groups)
df.to_csv('new_data.csv')