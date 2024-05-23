import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dic = {row.letter:row.code for (index, row) in data.iterrows()}
print(phonetic_dic)

word = input("Enter a word: ").upper()
try:
    output_list = [phonetic_dic[letter] for letter in word]
except KeyError:
    print("enter valid code")
else:
    print(output_list)
