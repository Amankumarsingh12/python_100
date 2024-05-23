import my_obj

here_name = [ "son", "father", "mother", "uncle", "neph" ]
here_val = [1, 2, 3, 4, 5]

me = []

for index in range(0, 5):
    me_loop = my_obj.Myname(here_name[index], here_val[index])
    me.append(me_loop)


print(me[2].value)

