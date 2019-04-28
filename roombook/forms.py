from django import forms
from .models import Bill



class BillForm(forms.ModelForm):
    name_of_the_bill = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter Your Bill Name'
        }
    ))
    bill_amount = forms.IntegerField()
    due_date = forms.IntegerField()

    class Meta:
        model = Bill
        fields = ('name_of_the_bill', 'bill_amount', 'due_date')



