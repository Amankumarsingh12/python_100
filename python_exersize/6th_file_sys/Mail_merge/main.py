#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("./Mail_merge/Input/Letters/starting_letter.txt","r") as file:
    data = file.read()
    #print(data)



with open("./Mail_merge/Input/Names/invited_names.txt", "r") as file:
    name_all = file.readlines()
    #print(name_all)


from final import Mail_for
mail = Mail_for()
for name in name_all :
    name = name.strip()
    data_2 = data.replace("[name]", name)
    mail.send_it(name, data_2)

