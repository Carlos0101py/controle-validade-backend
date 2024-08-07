from datetime import datetime


def datatime_to_days(expiry_date_at):

    format = "%Y-%m-%dT%H:%M:%S"

    today = datetime.now()
    expiry = datetime.strptime(expiry_date_at, format)
    days = expiry - today

    return days.days

