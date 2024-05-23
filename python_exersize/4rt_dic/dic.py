my_dic1 = {"name":"aman kr singh",
           1234 : "hii",
           "school": "pata nahi"}

my_dic1["new item"] = "added new iteam"

print(my_dic1)
print(my_dic1[1234])
print(my_dic1["name"])

for key in my_dic1:
    print(key)
    print(my_dic1[key])

travel_log = [
    {
        "country": "France",
        "city visited" : ["parish", "lille", "Dijon"],
        "total_visits" :12
    },

    {
        "country" : "india",
        "city visited" : ["patna","bhopal","delhi"],
        "total visit" : 22
    },

]


travel_log2 = {
    "country" : "Russia",
    "city visit"  : ["moscow", "saint petersburg"],
    "total visit" : 2,
}

travel_log.append(travel_log2)

print(travel_log)