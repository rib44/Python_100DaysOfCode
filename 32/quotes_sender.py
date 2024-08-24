import smtplib
import datetime as dt
from random import choice


from_email = ""
from_email_password = "";
to_email = ""

# select a quote
with open("quotes.txt", "r") as quotes:
    quote_list = quotes.readlines()
    quote = choice(quote_list)

# find day_of_week
day_of_week = dt.datetime.now().weekday()   # 0-6 (Monday-Sunday)

# choose the day to send
if day_of_week == 6:

    # create the SMTP connection
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=from_email, password=from_email_password)

        connection.sendmail(
            from_addr=from_email,
            to_addrs=to_email,
            msg=f"Subject:Today's Quote\n\n{quote}"
        )

