# CSV stands for Comma Separated Values
# import csv

# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if 'day' not in row:
#             temperature = int(row[1])
#             temperatures.append(temperature)
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(data)
print(data["temp"])