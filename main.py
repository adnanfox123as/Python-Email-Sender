import smtplib

sender_mail = input("Enter Sender Mail: ")
reciver_mail = input("Enter Receiver Mail: ")
title = input("Enter Title: ")
body = input("Enter Message: ")
psk = input("Enter Google App key: ")

text = f"Subject: {title}\n\n{body}"

x = smtplib.SMTP("smtp.gmail.com", 587)
x.starttls()
x.login(sender_mail,psk)
x.sendmail(sender_mail,reciver_mail,text)
