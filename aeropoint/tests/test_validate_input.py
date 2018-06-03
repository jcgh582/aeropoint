import datetime
import unittest.mock

from aeropoint.validate_input import is_valid_utc_iso8601

class TestIsValidIso8601Datetime(unittest.TestCase):
    def test_should_be_valid(self):
        iso8601_datetime_string = '2017-09-15T01:33:44Z'

        result = is_valid_utc_iso8601(iso8601_datetime_string)

        self.assertEquals(result, True)

    def test_should_be_invalid(self):
        iso8601_datetime_string = '2017-09-15T01:33:44'

        result = is_valid_utc_iso8601(iso8601_datetime_string)

        self.assertEquals(result, False)
