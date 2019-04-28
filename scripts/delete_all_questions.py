# scripts/delete_all_questions.py
import smtplib
from roombook.models import Bill
import datetime


def run():
    now = datetime.datetime.now()
    obj= Bill.objects.all()
    for i in obj:
        print(i.due_date)
        if i.due_date != now.day:
            s = smtplib.SMTP(host,port)  #enter mail server host and port number
            s.starttls()

            s.login("emailid", "password") #enter your email id and password.

            message = "Your "
            message= message + i.name_of_the_bill
            message+=" is due today. Please complete the payment! "

            s.sendmail("vivek.cs16@iitp.ac.in", "vivek.iitpatna@gmail.com", message)
            s.quit()
            break
        else:
            continue
run()
