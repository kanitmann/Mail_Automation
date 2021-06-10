import csv
import smtplib
import ssl
import email.utils

print("Initiated Mail Processing. Please be patient. . . ")
message = """Subject: Your Order has been placed!

Hi {name}, your order is {order}"""
i = 1

from_address = "your@email.com"
password = "your-password"
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(from_address, password)
    with open("file.csv") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for name, email, order in reader:
            server.sendmail(
                from_address,
                email,
                message,
            )
            print("\nSuccessfully mailed " + str(i) + " recipients.\n")
            i+=1
print("Successfully mailed all recipients.   :)")