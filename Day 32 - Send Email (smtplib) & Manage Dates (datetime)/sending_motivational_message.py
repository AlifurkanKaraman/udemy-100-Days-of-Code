import smtplib
import datetime as dt
import random

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()

my_email = "Your mail"
password = "Your password"

if day_of_week == 6:
    with open("quotes.txt", 'r') as quote_file:
        all_quotes = quote_file.readlines()
        random_quote = random.choice(all_quotes)
    print(random_quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="someone's email",
                            msg=f"Subject:Happy Sunday!\n\n{random_quote}")

