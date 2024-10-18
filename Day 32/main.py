import datetime as dt
import random
import smtplib

now = dt.datetime.now()
day_of_the_week = now.weekday()
if day_of_the_week == 5:
    with open("quotes.txt", "r") as quotes:
        data = quotes.readlines()
        todays_quote = random.choice(data)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user="atharvmitt2.0@gmail.com", password="flux divi mozm vvud")
        connection.sendmail(from_addr="atharvmitt2.0@gmail.com", to_addrs="atharvmitt@gmail.com", msg="Subject:Today's Quote!\n\n" + str(todays_quote))
