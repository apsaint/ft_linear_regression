from unittest import TestCase
from unittest.mock import patch, mock_open

from ft_linear_regression.data import get_file_path, get_data_from_csv, \
    get_thetas_from_csv, write_theta_data, clean_and_eval_data


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

    def test_clean_and_eval_data(self):
        """

        :return:
        """
        kms = ['km', '12345', '123456']
        prices = ['prices', '1234', '12345']

        kms, prices = clean_and_eval_data(kms, prices)

        self.assertEqual([12345, 123456], kms)
        self.assertEqual([1234, 12345], prices)

    @patch('ft_linear_regression.data.clean_and_eval_data',
           return_value=([12345, 123456], [1234, 12345]))
    @patch('os.path.isfile', return_value=True)
    def test_get_data_from_csv(self, mock_isfile, mock_eval_data):
        """
        Test that the method retrieve data from csv
        :param mock_open:
        """
        csv_file = 'csv_file'

        with patch('builtins.open', new_callable=mock_open()) as mock_csv:
            with patch('csv.reader') as mock_csv_reader:
                kms, prices = get_data_from_csv(csv_file)

                mock_isfile.assert_called_once_with(csv_file)

                mock_eval_data.assert_called_once()

                mock_csv.assert_called_once_with(csv_file, 'r')

                mock_csv_reader.assert_called_once()

    @patch('os.path.isfile', return_value=True)
    def test_get_thetas_from_csv(self, mock_isfile):
        """
        Test get thetas value from csv file method
        :param mock_isfile:
        """
        theta_file = 'theta_file'

        with patch('builtins.open', new_callable=mock_open()) as mock_csv:
            with patch('csv.reader') as mock_csv_reader:
                kms, prices = get_thetas_from_csv(theta_file)

                mock_isfile.assert_called_once_with(theta_file)

                mock_csv.assert_called_once_with(theta_file, 'r')

                mock_csv_reader.assert_called_once()

    def test_write_theta_data(self):
        """
        Test write theta data into a csv file
        """
        theta_file = 'theta_file'

        t0 = [0.1, 0.2, -0.8]
        t1 = [0.4, 0.3, -0.5]

        with patch('builtins.open', new_callable=mock_open()) as mock_csv:
            with patch('csv.writer') as mock_csv_writer:
                write_theta_data(t0, t1, theta_file)

                mock_csv.assert_called_once_with(theta_file, 'w')

                mock_csv_writer.assert_called_once()

                mock_csv_writer.return_value.writerow.assert_called_once_with([t0, t1])
