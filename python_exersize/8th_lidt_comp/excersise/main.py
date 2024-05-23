import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")


my_dict = {value["letter"]:value["code"] for (key, value) in data.iterrows()}
#print(my_dict)

my_inp = input("input a worrd ")

new_list = [my_dict[n.upper()] for n in my_inp]

print(new_list)