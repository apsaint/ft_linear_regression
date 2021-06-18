from unittest import TestCase
from unittest.mock import patch

from ft_linear_regression.precision import calc_precision


class TestPrecision(TestCase):
    """
    Class testing precision functions
    """

    @patch('ft_linear_regression.precision.calc_sum_of_squares_error', return_value=0.6789)
    @patch('ft_linear_regression.precision.calc_sum_of_squares_regression',
           return_value=0.3432)
    def test_calc_precision(self, mock_ssr, mock_sst):
        """
        Test calc precision method
        :param mock_ssr:
        :param mock_sst:
        """
        kms = [1234, 145656, 65678]
        prices = [12340, 1456, 6567]
        t0 = 0.4326
        t1 = 0.5432

        expected = 1 - (0.3432/0.6789)

        result = calc_precision(kms, prices, t0, t1)

        mock_ssr.assert_called_once_with(prices, kms, t0, t1)
        mock_sst.assert_called_once_with(prices)

        self.assertEqual(expected, result)
