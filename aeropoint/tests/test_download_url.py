import unittest.mock

from aeropoint.download_url import download_url

class TestDownloadUrl(unittest.TestCase):
    @unittest.mock.patch('aeropoint.download_url.urlretrieve')
    def test_should_get_correct_output_given_valid_input(self, mock_url_retrieve):
        mock_url_retrieve.return_value = ['filename']
        url = 'a/url/nybp257x.17o.gz'

        filename = download_url(url)

        mock_url_retrieve.assert_called_with(url, 'rawData/nybp257x.17o.gz')
        self.assertEquals(filename, 'filename')

    @unittest.mock.patch('aeropoint.download_url.urlretrieve')
    def test_should_propagate_exception_if_urlretrieve_throws(self, mock_url_retrieve):
        mock_url_retrieve.side_effect = Exception
        url = 'a/url/nybp257x.17o.gz'

        self.assertRaises(Exception, download_url, url)