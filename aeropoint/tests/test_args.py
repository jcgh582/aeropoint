import unittest.mock

from aeropoint.args import get_and_validate_args

class TestGetAndValidateArgs(unittest.TestCase):
    @unittest.mock.patch('aeropoint.args.get_args')
    def test_return_args_given_valid_args(self, mock_get_args):
        valid_args = ('base-station-id',
            '2017-09-14T23:11:22Z',
            '2017-10-14T23:11:22Z')
        mock_get_args.return_value = valid_args

        args_ = get_and_validate_args()

        self.assertEquals(args_, valid_args)

    @unittest.mock.patch('aeropoint.args.get_args')
    def test_should_throw_exception_given_invalid_start_datetime(self, mock_get_args):
        invalid_args = ('base-station-id',
            '2017-9-1',
            '2017-10-14T23:11:22Z')

        mock_get_args.return_value = invalid_args

        self.assertRaises(Exception, get_and_validate_args)

    @unittest.mock.patch('aeropoint.args.get_args')
    def test_should_throw_exception_given_invalid_end_datetime(self, mock_get_args):
        invalid_args = ('base-station-id',
            '2017-10-14T23:11:22Z',
            '2017-9-1')

        mock_get_args.return_value = invalid_args

        self.assertRaises(Exception, get_and_validate_args)