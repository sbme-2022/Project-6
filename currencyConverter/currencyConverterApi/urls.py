from django.urls import path,include
from . import views

urlpatterns = [
    path('currencyConverterApi/', views.currenciesAPI.as_view(), name='currencyConverter'),
]