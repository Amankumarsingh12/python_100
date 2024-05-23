#write a program to splite a bill with % of tips to people


bill=float(input("enter biil amount\n"))
per=int(input("enter percentage\n"))
people=int(input("people you want split\n"))


bill=(bill/people) * ((per/100)+1)

print(round(bill,2))
print("{:.2f}".format(bill))