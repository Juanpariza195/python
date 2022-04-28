from datetime import datetime, timedelta

date = datetime(2011, 4, 25, 0, 0)

def add(date):
    gigasecond = 1000000000
    intervalo = timedelta(0, gigasecond, 0)

    newDate = date + intervalo
    return newDate

print(add(date))