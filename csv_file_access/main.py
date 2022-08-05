# with open("weather_data.csv") as weather_data:
#     data = weather_data.readlines()
#     print(data) # ['day,temp,condition\n', 'Monday,12,Sunny\n', 'Tuesday,14,Rain\n',...
#     #readlines() would convert each row of the file to a string list element

# import csv
#
# with open("weather_data.csv") as weather_data:
#     data = csv.reader(weather_data)
#     #print(data) # this would create a csv reader iterator object which can be iterated
#
#     temperature = []
#     for row in data:
        # print(row)  # Now each row is a seperate list of seperate string element, which is easier to work  than before
#         #['day', 'temp', 'condition'] ['Monday', '12', 'Sunny']
#         #print(row[1])
#         if row[1] != 'temp': # Retrieving temparatures from data
#             temperature.append(int(row[1]))
#
#     print(temperature)

import pandas
# data = pandas.read_csv('weather_data.csv')
#print(data)
#print(type(data)) # <class 'pandas.core.frame.DataFrame'>
#print(data['temp'])
#print(type(data['temp'])) # <class 'pandas.core.series.Series'>
# So the whole table returned by pandas is a dataframe and each column of that dataframe is a series which is similar to
# list

# data_dict =data.to_dict() # convert the dataframe into a dictionary
# print(data_dict)
#
# temp_list = data['temp'].tolist() # converting series into a list
# print(temp_list)
#
# print(data['temp'].mean())
#print(data['temp'].max())

# To get a column from the dataframe
# print(data['condition']) # the way we retrieve a data from dictionary
# print(data.condition)

# get row from the dataframe
#pull the row where day is Monday
#print(data[data['day'] == 'Monday']) # 1st hold the dataframe; inside that hold the column and then give the condition

#which row of data has the highest temperature in a week?
# print(data[data['temp'] == data['temp'].max()])
# print(data[data.temp == data.temp.max()])

#hold the data of a particular row
# monday = data[data.day == 'Monday']
# # print(monday.condition)
# #print(data[data.day == 'Monday']['condition'])
#
# #convert monday temperatute to ferenhite
# celcius_temp = monday.temp
# print(celcius_temp * (9/5) + 32)


