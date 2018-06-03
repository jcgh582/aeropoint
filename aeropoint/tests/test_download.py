import unittest.mock

from aeropoint.download import download

base_station_id = 'nybp'
start_datetime = '2018-06-01T01:11:22Z'
end_datetime = '2018-06-01T05:33:44Z'

decompressed_filename = 'filename'
downloaded_filename = 'filename.gz'
generated_urls = ['generated_url1/filename.gz']

class TestDownload(unittest.TestCase):
    @unittest.mock.patch('aeropoint.download.generate_urls')
    @unittest.mock.patch('aeropoint.download.download_url')
    @unittest.mock.patch('aeropoint.download.decompress_gz_file')
    def test_should_return_filenames(
        self,
        mock_decompress_gz_file,
        mock_download_url,
        mock_generate_urls):

        mock_decompress_gz_file.return_value = decompressed_filename
        mock_download_url.return_value = downloaded_filename
        mock_generate_urls.return_value = generated_urls

        filenames = download(base_station_id, start_datetime, end_datetime)

        self.assertEquals(filenames, [decompressed_filename])

    @unittest.mock.patch('aeropoint.download.generate_urls')
    @unittest.mock.patch('aeropoint.download.download_url')
    @unittest.mock.patch('aeropoint.download.decompress_gz_file')
    def test_should_call_generate_urls_with_correct_args(
        self,
        mock_decompress_gz_file,
        mock_download_url,
        mock_generate_urls):

        mock_decompress_gz_file.return_value = decompressed_filename
        mock_download_url.return_value = downloaded_filename
        mock_generate_urls.return_value = generated_urls

        download(base_station_id, start_datetime, end_datetime)

        mock_generate_urls.assert_called_with(base_station_id, start_datetime, end_datetime)

    @unittest.mock.patch('aeropoint.download.generate_urls')
    @unittest.mock.patch('aeropoint.download.download_url')
    @unittest.mock.patch('aeropoint.download.decompress_gz_file')
    def test_should_call_download_url_with_correct_args(
        self,
        mock_decompress_gz_file,
        mock_download_url,
        mock_generate_urls):

        mock_decompress_gz_file.return_value = decompressed_filename
        mock_download_url.return_value = downloaded_filename
        mock_generate_urls.return_value = generated_urls

        download(base_station_id, start_datetime, end_datetime)

        mock_download_url.assert_called_with(generated_urls[0])

    @unittest.mock.patch('aeropoint.download.generate_urls')
    @unittest.mock.patch('aeropoint.download.download_url')
    @unittest.mock.patch('aeropoint.download.decompress_gz_file')
    def test_should_call_decompress_gz_file_with_correct_args(
        self,
        mock_decompress_gz_file,
        mock_download_url,
        mock_generate_urls):

        mock_decompress_gz_file.return_value = decompressed_filename
        mock_download_url.return_value = downloaded_filename
        mock_generate_urls.return_value = generated_urls

        download(base_station_id, start_datetime, end_datetime)

        mock_decompress_gz_file.assert_called_with(downloaded_filename)