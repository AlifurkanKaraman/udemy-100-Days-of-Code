# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)


# import csv
# Without pandas library
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)


import pandas

# With pandas library
# data = pandas.read_csv("weather_data.csv")
# print(data)

# Find average value
# temp_list = data['temp'].to_list()
# print(sum(temp_list) / len(temp_list))

# Find average value with mean() function
# t_list = data['temp'].mean()
# print(t_list)

# Find the maximum value of series
# max_value = data['temp'].max()
# print(max_value)

# Get Data in Columns
# print(data['condition'])
# print(data.condition)

# Get Data in Rows
# print(data[data.day == "Monday"])
# print(data[data.temp == data['temp'].max()])

# Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_file.csv")

squirrel_data = pandas.read_csv("Squirrel_Data.csv")
gray_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
black_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])
red_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
print(gray_squirrels_count)
print(black_squirrels_count)
print(red_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Black", "Cinnamon"],
    "Count": [gray_squirrels_count, black_squirrels_count, red_squirrels_count]
}
data = pandas.DataFrame(data_dict)
data.to_csv("New_squirrels_data.csv")

gray_squirrel = squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"]
print(gray_squirrel)
print(squirrel_data["Primary Fur Color"].count)
print(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])