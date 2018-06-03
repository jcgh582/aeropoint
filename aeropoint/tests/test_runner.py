import unittest.mock

from aeropoint.runner import run
from aeropoint.download import download
from aeropoint.merge import merge

from nose.tools import set_trace

filenames = ['filename1', 'filename2']

class TestRunner(unittest.TestCase):
    @unittest.mock.patch('aeropoint.runner.download')
    @unittest.mock.patch('aeropoint.runner.merge')
    def test_should_call_correct_functions(
        self,
        mock_merge,
        mock_download):

        mock_download.return_value = filenames
        mock_merge.return_value = None

        base_station_id = 'nybp'
        start_datetime = '2018-06-01T01:11:22Z'
        end_datetime = '2018-06-01T05:33:44Z'

        run(base_station_id, start_datetime, end_datetime)

        mock_download.assert_called_with(base_station_id, start_datetime, end_datetime)
        mock_merge.assert_called_with(filenames)