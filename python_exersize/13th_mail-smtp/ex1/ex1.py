import datetime as dt
import smtplib
import random

my_email = "aksinghn97@gmail.com"
passWord = "bvmg vzku npsz mtpg"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 1:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=passWord)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs="amansinghas1536610@gmail.com", 
            msg=f"Subject:Monday Motivation\n\n{quote}"
            )
    
    
        

