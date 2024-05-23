import pandas


# data = pandas.read_csv("data.csv")

# print(data["temp"])

# # print(data["temp"].mean())

# print(data[data.day == "Monday"])

# #data.temp.max()
# print(data[data.temp == data.temp.max()])

data_dict = {
    "student" : ["Any", "James", "Angela"],
    "score" : [76, 56, 65]

}

data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_written.csv")