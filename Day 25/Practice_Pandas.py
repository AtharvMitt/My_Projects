import csv
import pandas

data = pandas.read_csv("weather_data.csv")
temp_list = data["temp"].to_list()
Sum_temp = sum(temp_list)
len_temp = len(temp_list)
av = Sum_temp/len_temp
print(av)

print(max(temp_list))