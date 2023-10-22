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
# print(data["temp"])

# convert Dataframe object data to a dictionary
data_dict = data.to_dict()
print(data_dict)

# convert Series object data['temp'] to a list
temp_list = data["temp"].to_list()


# temp_average = sum(temp_list) / len(temp_list)
# print(temp_average)
# line below does the same thing as the two lines above
print(temp_list)


print(data["temp"].mean())
print(data['temp'].max())

# Behind the scenes the pandas library converts column headings into attributes so the next lines are valid
print(data.condition)
print(data.temp)

# Get Data in Row
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.temp[0])
monday_temp_fahrenheit = (monday.temp[0] * 9 / 5) + 32
print(monday_temp_fahrenheit)


# Create a dataframe from scratch
data_dict = {
    "student": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

dataframe = pandas.DataFrame(data_dict)
print(dataframe)

# Store data from into csv file
dataframe.to_csv("new_data.csv")
