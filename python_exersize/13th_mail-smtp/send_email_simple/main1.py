import smtplib

my_email = "aksinghn97@gmail.com"
passWord = "bvmg vzku npsz mtpg"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=passWord)

connection.sendmail(from_addr=my_email, to_addrs="eng2aksingh@gmail.com", msg="Subject:hello\n\nhi ji")
connection.close()