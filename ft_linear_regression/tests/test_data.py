from unittest import TestCase
from unittest.mock import patch

from ft_linear_regression.data import get_file_path


class TestData(TestCase):
    """
    Class testing data functions
    """

    @patch('os.path.join', return_value='cur_path/my_file')
    @patch('os.path.dirname', return_value='cur_path/')
    def test_get_file_path(self, mock_dirname, mock_join):
        """
        Testing get_file_path method
        :param mock_dirname: mock dirname method
        :param mock_join: mock join method
        """
        file = 'my_file'
        cur_path = 'cur_path/'

        file_path = get_file_path(file)

        mock_dirname.assert_called_once()
        mock_join.assert_called_once_with(cur_path, file)
        self.assertEqual('cur_path/my_file', file_path)

    @patch('builtins.open')
    def test_get_data_from_csv(self, mock_open):
        """
        Test that the method retrieve data from csv
        :param mock_open:
        """


