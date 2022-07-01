from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import View
import sys
sys.path.append("..")
from fetchFromApi.models import currencies

class currenciesAPI(View):    
    def get(self, request):
            FromCurrenncyQuery=request.GET.get('From')
            ToCurrenncyQuery=request.GET.get('To')
            selectedQuery = currencies.objects.get(fromCurrency='EGP',toCurrency=ToCurrenncyQuery)
            selectedQuery2 = currencies.objects.get(fromCurrency='EGP',toCurrency=FromCurrenncyQuery)

            data = {
                'From':FromCurrenncyQuery,
                'To':ToCurrenncyQuery,
                'rate':selectedQuery.rate/selectedQuery2.rate
            }

            return JsonResponse(data)