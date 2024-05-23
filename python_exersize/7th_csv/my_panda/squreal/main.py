import pandas

data = pandas.read_csv("Squirrel_Data.csv")

grey_sq_count =  len(data[data["Primary Fur Color"] == "Gray"])
black_sq_count = len(data[data["Primary Fur Color"] == "Black"])
Cinnamon_sq_count = len(data[data["Primary Fur Color"] == "Cinnamon"])

data_dict = {
    "Fur color" : ["Gray", "Black", "Cinnamon"],
    "Count": [grey_sq_count, black_sq_count, Cinnamon_sq_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squrel_count.csv")