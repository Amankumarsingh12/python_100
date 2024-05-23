# try:        #it fail 
#     file = open("a_file.txt")
# except:      #then run thus
#     print("hii")

try:
    file = open("a_file.txt")
    a_dist = {"key": "value"}
    print(a_dist["key"])
except FileNotFoundError:   #only exept file not found error
    file = open("a_file.txt", "w")
    file.write("ama")
except KeyError as error_msg:
    print(f"aman{error_msg}")
else:
    content = file.read()
    print(content)
finally:
    file.close()

    