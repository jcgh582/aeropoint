from aeropoint.hourly_datetime_iterator import hourly_datetime_iterator
from aeropoint import helpers

BASE_URL = 'ftp://www.ngs.noaa.gov/cors/rinex/'

def create_url(base_station_id, datetime_):
    day_of_year = helpers.get_day_of_year_as_string(datetime_)

    url = BASE_URL
    url += helpers.get_year_as_string(datetime_) + '/'
    url += day_of_year + '/'
    url += base_station_id + '/'
    url += base_station_id \
        + day_of_year \
        + helpers.convert_hour_to_letter(helpers.get_hour_as_string(datetime_)) \
        + '.' + helpers.get_year_shorthand_as_string(datetime_) + 'o.gz'

    return url

def generate_urls(base_station_id, start_datetime, end_datetime):
    sdt = helpers.convert_iso8601_to_datetime(start_datetime)
    edt = helpers.convert_iso8601_to_datetime(end_datetime)

    for datetime_ in hourly_datetime_iterator(sdt, edt):
        yield create_url(base_station_id, datetime_)
