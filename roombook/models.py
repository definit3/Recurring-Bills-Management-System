from django.db import models



class Bill(models.Model):
    name_of_the_bill = models.CharField(max_length=200, null=True, default="")
    bill_amount = models.IntegerField()
    due_date  = models.IntegerField()

    def __str__(self):
        return self.name_of_the_bill
