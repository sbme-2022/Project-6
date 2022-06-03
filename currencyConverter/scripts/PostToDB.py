from fetchFromApi.models import currencies
import requests
from currencyConverter.settings import API_KEY


def FetchFromApi():
    url ="https://api.apilayer.com/exchangerates_data/latest?&base=EGP"
    payload = {}
    headers= {
    "apikey":API_KEY
    }
    response = requests.request("GET", url, headers=headers, data = payload)
    result = response.json()
    return result
def run():
    fetchedData=FetchFromApi()
    for currency in fetchedData['rates']:
        currencies.objects.create(fromCurrency='EGP',toCurrency=currency, rate=fetchedData['rates'][currency])
        print(currency,fetchedData['rates'][currency])
