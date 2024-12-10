##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import random
import pandas as pd
import smtplib
import datetime as dt
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

my_email = "tutirootie@gmail.com"
password = "gksqgxvsirvevlgk"

msg = MIMEMultipart()
msg['From'] = my_email
msg['Subject'] = "Happy birthday"

data = pd.read_csv('birthdays.csv')
now = dt.datetime.now()

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)

    for index, row in data.iterrows():
        if row.get('day') == now.day and row.get('month') == now.month:
            msg["To"] = row.get("email")
            with open(f'letter_templates/letter_{random.randint(1, 3)}.txt') as file:
                body = file.read().replace("[NAME]", row.get('name'))
            msg.attach(MIMEText(body, 'plain'))
            connection.sendmail(from_addr=my_email, to_addrs=row.get('email'), msg=msg.as_string())




