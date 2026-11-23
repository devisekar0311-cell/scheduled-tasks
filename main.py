import os
import smtplib

import pandas
import datetime as dt
import random



now = dt.datetime.now()
today_month = now.month
today_day = now.day
today_tuple=(today_month,today_day)


# HINT 2: Use pandas to read the birthdays.csv
data=pandas.read_csv('birthdays.csv')
birthday_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

# if (today_month, today_day) in birthdays_dict:
if today_tuple in birthday_dict:
    # 1. Get the birthday person's record
    birthday_person = birthday_dict[(today_month, today_day)]

    # 2. Pick a random letter template
    random_num = random.randint(1, 3)
    file_path = f"letter_templates/letter_{random_num}.txt"

    # 3. Open and read the letter content as a string
    with open(file_path) as letter_file:
        content = letter_file.read()

    # 4. Replace [NAME] with the actual name from the dictionary
    new_letter = content.replace("[NAME]", birthday_person["name"])

    # 5. Print or check the updated letter
    print(new_letter)
   MY_EMAIL = os.environ.get("MY_EMAIL")
   MY_PASSWORD = os.environ.get("MY_PASSWORD")
   message = f"Subject: Happy Birthday\n\n{new_letter}"

    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.starttls()
        smtp.login(user=MY_EMAIL, password=MY_PASSWORD)
        smtp.sendmail(from_addr=MY_EMAIL,to_addrs=birthday_person["email"], msg=message)
        print(f"Birthday email sent to {birthday_person['name']}!")














