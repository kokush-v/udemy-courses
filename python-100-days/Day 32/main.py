import random
import  smtplib
import datetime as dt
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

with open('quotes.txt') as file:
    quotes = [line.strip() for line in file.readlines()]

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
my_email = "tutirootie@gmail.com"
password = "gksqgxvsirvevlgk"

now = dt.datetime.now()

msg = MIMEMultipart()
msg['From'] = my_email
msg['To'] = "witalik.logoyda@gmail.com"
msg['Subject'] = "Test Email"
body = f"Today is {weekdays[now.weekday()]}\n{random.choice(quotes)}"
msg.attach(MIMEText(body, 'plain'))


with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs='witalik.logoyda@gmail.com', msg=msg.as_string())