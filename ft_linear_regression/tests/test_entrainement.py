from unittest import TestCase
from unittest.mock import patch

from ft_linear_regression.entrainement import estimate_price_calc, read_data

mock_csv_file_content = '0,0 \
						 1,1'


class TestBasicFunction(TestCase):
	"""
	Class testing basic functions
	"""

	def test_estimatePrice_calc(self):
		kms = 100
		th0 = 1
		th1 = 1

		price = estimate_price_calc(kms, th0, th1)
		self.assertEqual(price, float(101))

	@patch('csv.DictReader', return_value=[('0','0'), ('1','1')])
	@patch('builtins.open', read_data=mock_csv_file_content)
	def test_read_data_ok(self, mock_open, mock_dictreader):
		list = read_data('file')

		mock_open.assert_called_once()
		mock_dictreader.assert_called_once()
		self.assertEqual(len(list), 2)

	@patch('builtins.open', side_effect=IOError())
	def test_read_data_file_not_found(self, mock_open):
		list = read_data('file')

		mock_open.assert_called_once()
		self.assertEqual(len(list), 0)
