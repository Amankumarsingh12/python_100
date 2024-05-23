from datetime import datetime
import pandas
import random
import smtplib

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for(index, data_row) in data.iterrows()}


def sendEmail(content):
    my_email = "aksinghn97@gmail.com"
    passWord = "bvmg vzku npsz mtpg"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=passWord)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs="amansinghas1536610@gmail.com", 
            msg=f"Subject:Happy birthday\n\n{content}"
            )



if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        content = letter_file.read()
        content = content.replace("[NAME]", birthday_person["name"])
        content = content.replace("Angela", "subham")
        sendEmail(content)
