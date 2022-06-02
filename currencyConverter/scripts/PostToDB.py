from fetchFromApi.models import currencies
import requests
from currencyConverter.settings import API_KEY



def run():
    url ="https://api.apilayer.com/exchangerates_data/latest?&base=EGP"
    payload = {}
    headers= {
    "apikey":API_KEY
    }
    response = requests.request("GET", url, headers=headers, data = payload)
    result = response.json()
    for currency in result['rates']:
        currencies.objects.create(fromCurrency='EGP',toCurrency=currency, rate=result['rates'][currency])
        print(currency,result['rates'][currency])
