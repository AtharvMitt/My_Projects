import datetime as dt
import pandas
import random
import smtplib

MY_EMAIL = "atharvmitt2.0@gmail.com"
MY_PASSWORD = "flux divi mozm vvud"
now = dt.datetime.now()
Date = now.day
Month = now.month
today = (Month, Date)

data = pandas.read_csv("birthdays.csv")

birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    print(birthday_person["name"])
    file_path = f"letter_{random.randint(1,3)}.txt"
    with open(file_path, "r") as letter_file:
        contents = letter_file.read()
        contents2 = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=birthday_person["email"],
                            msg="Subject:Happy Birthday!\n\n" + str(contents2)
                            )
