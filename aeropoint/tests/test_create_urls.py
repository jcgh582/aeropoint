import unittest

from aeropoint.create_urls import create_urls

class TestCreateUrls(unittest.TestCase):
    def test_should_get_correct_output_given_valid_input(self):
        base_station_id = 'nybp'
        start_datetime = '2017-09-14T23:11:22Z'
        end_datetime = '2017-09-15T01:33:44Z'

        urls = create_urls(base_station_id, start_datetime, end_datetime)

        self.assertEquals(urls, [
            'ftp://www.ngs.noaa.gov/cors/rinex/2017/257/nybp/nybp257x.17o.gz',
            'ftp://www.ngs.noaa.gov/cors/rinex/2017/258/nybp/nybp258a.17o.gz',
            'ftp://www.ngs.noaa.gov/cors/rinex/2017/258/nybp/nybp258b.17o.gz'])

