# # CSV stands for Comma Separated Values
# # import csv
#
# # with open("weather_data.csv") as data_file:
# #     data = data_file.readlines()
# #     print(data)
#
# # with open("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     temperatures = []
# #     for row in data:
# #         if 'day' not in row:
# #             temperature = int(row[1])
# #             temperatures.append(temperature)
# #     print(temperatures)
#
import pandas
#
# data = pandas.read_csv("weather_data.csv")
# # print(data)
# # print(data["temp"])
#
# # convert Dataframe object data to a dictionary
# data_dict = data.to_dict()
# print(data_dict)
#
# # convert Series object data['temp'] to a list
# temp_list = data["temp"].to_list()
#
#
# # temp_average = sum(temp_list) / len(temp_list)
# # print(temp_average)
# # line below does the same thing as the two lines above
# print(temp_list)
#
#
# print(data["temp"].mean())
# print(data['temp'].max())
#
# # Behind the scenes the pandas library converts column headings into attributes so the next lines are valid
# print(data.condition)
# print(data.temp)
#
# # Get Data in Row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# print(monday.temp[0])
# monday_temp_fahrenheit = (monday.temp[0] * 9 / 5) + 32
# print(monday_temp_fahrenheit)
#
#
# # Create a dataframe from scratch
# data_dict = {
#     "student": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# dataframe = pandas.DataFrame(data_dict)
# print(dataframe)
#
# # Store data from into csv file
# dataframe.to_csv("new_data.csv")


# Challenge
squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
primary_fur_colors = squirrel_data["Primary Fur Color"].to_list()
colors_count = [0, 0, 0]
for fur_color in primary_fur_colors:
    if fur_color == "Gray":
        colors_count[0] += 1
    elif fur_color == "Cinnamon":
        colors_count[1] += 1
    elif fur_color == "Black":
        colors_count[2] += 1


squirrel_count_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": colors_count
}

data_frame = pandas.DataFrame(squirrel_count_dict)


data_frame.to_csv("squirrel_count.csv")

# Solution from video
grey_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])

squirrel_count_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(squirrel_count_dict)
df.to_csv("squirrel_count.csv")
