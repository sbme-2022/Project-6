from fetchFromApi.models import currencies
import requests
from currencyConverter.settings import API_KEY



def run():
    Curriencies=["AED","AUD","CAD","EGP","EUR","GBP","INR","PLN","SAR","ZAR"]
    for from_currency in Curriencies:
            for to_currency in Curriencies:
                url = "https://api.apilayer.com/exchangerates_data/convert?to="+to_currency+"&from="+from_currency+"&amount=20"
                payload = {}
                headers= {
                "apikey":API_KEY
                }
                response = requests.request("GET", url, headers=headers, data = payload)
                result = response.json()
                currencies.objects.create(fromCurrency=from_currency,toCurrency=to_currency, rate=result['info']['rate'])


