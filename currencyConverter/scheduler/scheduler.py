from fetchFromApi.models import currencies
from currencyConverter.settings import API_KEY
from apscheduler.schedulers.background import BackgroundScheduler
import sys
sys.path.append("..")
from scripts.PostToDB import FetchFromApi

# This is the function you want to schedule - add as many as you want and then register them in the start() function below
def update_currencies():
    fetchedData=FetchFromApi()
    for currency in fetchedData['rates']:
        currencies.objects.filter(fromCurrency='EGP',toCurrency=currency).update(rate=fetchedData['rates'][currency])

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(update_currencies, 'interval', hours=6)
    scheduler.start()
    print("Scheduler started...", file=sys.stdout)