import datetime
import unittest

from aeropoint.hourly_datetime_iterator import hourly_datetime_iterator

class TestHourlyDatetimeIterator(unittest.TestCase):
    def test_should_be_able_to_handle_midnight(self):
        start_datetime = \
            datetime.datetime(2017, 9, 14, 23, 11, 22, tzinfo=datetime.timezone.utc)
        end_datetime = \
            datetime.datetime(2017, 9, 15, 1, 33, 44, tzinfo=datetime.timezone.utc)

        results = [result for result in hourly_datetime_iterator(start_datetime, end_datetime)]

        expected_results = [
            datetime.datetime(2017, 9, 14, 23, 0, 0, tzinfo=datetime.timezone.utc),
            datetime.datetime(2017, 9, 15, 0, 0, 0, tzinfo=datetime.timezone.utc),
            datetime.datetime(2017, 9, 15, 1, 0, 0, tzinfo=datetime.timezone.utc)]

        self.assertEquals(results, expected_results)
