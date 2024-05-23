#print("amAn".lower().count("a"))

name1=input("your name ")
name2=input("your partener ")

score1=0

score1 += name1.lower().count("l")
score1 += name1.lower().count("o")
score1 += name1.lower().count("v")
score1 += name1.lower().count("e")

score1 += name1.lower().count("t")
score1 += name1.lower().count("r")
score1 += name1.lower().count("u")
score1 += name1.lower().count("e")

score2=0
score2 += name2.lower().count("l")
score2 += name2.lower().count("o")
score2 += name2.lower().count("v")
score2 += name2.lower().count("e")

score2 += name2.lower().count("t")
score2 += name2.lower().count("r")
score2 += name2.lower().count("u")
score2 += name2.lower().count("e")

print(str(score1)+str(score2))