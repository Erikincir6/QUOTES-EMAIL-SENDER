import random
import datetime as dt
import smtplib


my_email = "erkan09@hotmail.co.uk"
password = "geliveringari9"


now = dt.datetime.now()
day_of_weeek = now.weekday()
if day_of_weeek == 1:
    with open("quotes.txt") as quotes_file:
        quotes = quotes_file.readlines()
        day_quotes = random.choice(quotes)

    with smtplib.SMTP("smtp-mail.outlook.com",587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="erkan0901@gmail.com", msg=f"Subject:quotes of the day\n\n.{day_quotes}")