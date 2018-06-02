import datetime
import unittest
import unittest.mock

from aeropoint.generate_urls import generate_urls
from aeropoint.hourly_datetime_iterator import hourly_datetime_iterator

class TestGenerateUrls(unittest.TestCase):
    def setUp(self):
        hourly_datetime_iterator = unittest.mock.Mock(return_value=[
            datetime.datetime(2017, 9, 14, 23, 0, 0, tzinfo=datetime.timezone.utc),
            datetime.datetime(2017, 9, 15, 0, 0, 0, tzinfo=datetime.timezone.utc),
            datetime.datetime(2017, 9, 15, 1, 0, 0, tzinfo=datetime.timezone.utc)])

    def test_should_get_correct_output_given_valid_input(self):
        base_station_id = 'nybp'
        start_datetime = '2017-09-14T23:11:22Z'
        end_datetime = '2017-09-15T01:33:44Z'

        urls = [url for url in generate_urls(base_station_id, start_datetime, end_datetime)]

        self.assertEquals(urls, [
            'ftp://www.ngs.noaa.gov/cors/rinex/2017/257/nybp/nybp257x.17o.gz',
            'ftp://www.ngs.noaa.gov/cors/rinex/2017/258/nybp/nybp258a.17o.gz',
            'ftp://www.ngs.noaa.gov/cors/rinex/2017/258/nybp/nybp258b.17o.gz'])

