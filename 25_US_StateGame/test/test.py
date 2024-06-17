# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#
#     for row in data:
#         print(row)
#
# print(temperatures)
#
import pandas as pd
#
#
# data = pandas.read_csv("weather_data.csv")
# print(data)
# print(data['temp'])

# data_dict = data.to_dict()
# print(data.temp.max())
# print(data[data.temp == data.temp.max()])
# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# print(monday_temp*(9/5) + 32)

# create a dataframe
# data_dict = {
#     "students": ["Amy", "James", "Angels"],
#     "scores": [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")
# print(data)

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240613.csv")


grey_df = data[data["Primary Fur Color"] == "Gray"].shape[0]
black_df = data[data["Primary Fur Color"] == "Black"].shape[0]
cinnamon_df = data[data["Primary Fur Color"] == "Cinnamon"].shape[0]

data_dict = {
    "Fur color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_df, black_df, cinnamon_df]
}

pd_df = pd.DataFrame(data_dict)

print(pd_df)


