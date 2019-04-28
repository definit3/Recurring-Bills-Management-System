from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import  BillForm
from .models import Bill
from django.http import HttpResponse
import datetime


class billbookView(TemplateView):

    template_name = 'roombook/homeallincall.html'
    template_name2 = 'roombook/home2allincall.html'

    def get(self, request):
        form = BillForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):

        form = BillForm(request.POST)
        if form.is_valid():
            form.save()
            delta = 200
            args = {'form': form, 'days': delta}
            return render(request, self.template_name2, args)

        else:
            return HttpResponse('Form is not valid')