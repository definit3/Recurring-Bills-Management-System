from django.urls import path
from .views import  billbookView


urlpatterns = [
    path('', billbookView.as_view(), name='roombook'),
]
