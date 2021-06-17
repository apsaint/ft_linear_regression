from unittest import TestCase
from unittest.mock import patch

from ft_linear_regression.estimate import get_user_km, estimate_price_calc

kms = [240000, 139800, 150500, 185530, 176000]
prices = [3650, 3800, 4400, 4450, 5250]

th0 = 0.9392906118825314
th1 = -1.0035016965560926


class TestEstimate(TestCase):
    """
    Class testing estimate functions
    """

    @patch('builtins.input', return_value='20000')
    def test_get_user_km_ok(self, mock_input):
        """
        Test a success km input retrieve from user
        :param mock_input:
        """
        input_km = get_user_km()

        self.assertEqual(20000, input_km)

    @patch('ft_linear_regression.estimate.denormalize')
    @patch('ft_linear_regression.estimate.normalize')
    def test_estimate_price_calc(self, mock_normalize, mock_denormalize):
        """
        Test price estimation function
        :return:
        """
        input_kms = 20000

        price = estimate_price_calc(kms, prices, input_kms, th0, th1)

        mock_normalize.assert_called_once_with(kms, input_kms)
        mock_denormalize.assert_called_once()
