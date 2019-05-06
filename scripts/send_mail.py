import smtplib
from roombook.models import Bill
import datetime


def run():
    now = datetime.datetime.now()
    obj= Bill.objects.all()
    print(now.day)
    for i in obj:
        print(i.due_date)
        if i.due_date == now.day:
            print("YES")
            s = smtplib.SMTP('smtp.gmail.com',587)  #enter mail server host and port number
            s.starttls()

            s.login("id", "password") #enter your email id and password.

            message = "Your "
            message= message + i.name_of_the_bill
            message+=" is due today. Please complete the payment! \n"
            message+= "Regards.. Allincall Team"
            s.sendmail("roguedoppelganger@gmail.com", i.email_id, message)
            s.quit()
            break
        else:
            continue
