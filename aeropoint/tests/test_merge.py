import subprocess
import unittest.mock

from aeropoint.merge import merge

filenames = ['filename1', 'filename2']
merged_file_contents = 'merged_file_contents'

class MockedPopenSuccessful():
    def __init__(self):
        self.returncode = 0

    def communicate(self):
        return merged_file_contents, ''

class MockedPopenUnsuccessful():
    def __init__(self):
        self.returncode = 1

    def communicate(self):
        return merged_file_contents, ''

class TestMerge(unittest.TestCase):
    @unittest.mock.patch('aeropoint.merge.write_to_file')
    @unittest.mock.patch('aeropoint.merge.subprocess.Popen')
    def test_write_correct_output_to_file(self, mock_popen, mock_write_to_file):
        mock_write_to_file.return_value = None
        mock_popen.return_value = MockedPopenSuccessful()

        merge(filenames)

        mock_write_to_file.assert_called_with(merged_file_contents, 'output/example.obs')

    @unittest.mock.patch('aeropoint.merge.write_to_file')
    @unittest.mock.patch('aeropoint.merge.subprocess.Popen')
    def test_run_correct_bash_command(self, mock_popen, mock_write_to_file):
        mock_write_to_file.return_value = None
        mock_popen.return_value = MockedPopenSuccessful()

        merge(filenames)

        mock_popen.assert_called_with(['./teqc', 'filename1', 'filename2'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    @unittest.mock.patch('aeropoint.merge.write_to_file')
    @unittest.mock.patch('aeropoint.merge.subprocess.Popen')
    def test_should_throw_exception_if_returncode_is_non_zero(self, mock_popen, mock_write_to_file):
        mock_write_to_file.return_value = None
        mock_popen.return_value = MockedPopenUnsuccessful()

        self.assertRaises(Exception, merge, filenames)