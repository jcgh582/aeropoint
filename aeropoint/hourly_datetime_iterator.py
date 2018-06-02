import datetime

def hourly_datetime_iterator(start_datetime, end_datetime):
    print(start_datetime)
    print(end_datetime)
    time_delta = datetime.timedelta(hours=1)

    datetime_ = datetime.datetime(
        start_datetime.year,
        start_datetime.month,
        start_datetime.day,
        start_datetime.hour,
        tzinfo=datetime.timezone.utc)

    while datetime_ < end_datetime:
        yield datetime_
        datetime_ += time_delta
    return
