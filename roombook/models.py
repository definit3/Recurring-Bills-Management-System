from django.db import models



class Bill(models.Model):
    name_of_the_bill = models.CharField(max_length=200, null=True, default="")
    bill_amount = models.CharField(max_length=200, null=True, default="")
    due_date  = models.CharField(max_length=200, null=True, default="")
    email_id = models.CharField(max_length=200, null=True, default="")

    def __str__(self):
        return self.name_of_the_bill
