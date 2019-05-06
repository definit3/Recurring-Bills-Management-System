from django import forms
from .models import Bill



class BillForm(forms.ModelForm):
    name_of_the_bill = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter Your Bill Name'
        }
    ))
    bill_amount = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter the bill amount'
        }
    ))
    due_date = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter Day number( e.g "5")'
        }
    ))
    email_id = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter Your email-id'
        }
    ))

    class Meta:
        model = Bill
        fields = ('name_of_the_bill', 'bill_amount', 'due_date', 'email_id')



