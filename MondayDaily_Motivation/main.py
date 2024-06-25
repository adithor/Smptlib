import smtplib
import datetime as dt
import random

my_email = "senders_email@domainName.com"
password = "Password"

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 0:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)

#Connectiong to my mail server
connection = smtplib.SMTP("smtp.gmail.com", 587, timeout=10) 

#start tls(Transport Layer Security)
connection.starttls()
connection.login(user=my_email, password= password)
connection.sendmail(
    from_addr=my_email,
    to_addrs="receivers_mail@domainName.com",
    msg=f"Subject:!!!DAILY  MONDAY MOTIVATION!!!\n\n{quote}")
connection.close()
