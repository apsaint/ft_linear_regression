from ft_linear_regression.data import get_file_path, get_data_from_csv, get_thetas_from_csv
from ft_linear_regression.estimate import estimate_price_calc


def calc_sum_of_squares_regression(prices: list, kms: list, t0: float, t1: float) -> float:
    """
    Calculate sum of squares
    :param prices:
    :param kms:
    :param t0:
    :param t1:
    :return: ssr value in float
    """
    sum_of_regression = sum(map(lambda km, price: pow(
        price - estimate_price_calc(kms, prices, km, t0, t1), 2
    ), kms, prices))
    return sum_of_regression


def calc_sum_of_squares_error(prices: list) -> float:
    """
    Calculate error estimation
    :param prices:
    :return: error float
    """
    price_average = sum(prices) / len(prices)
    sum_of_error = sum(map(lambda price: pow(price - price_average, 2), prices))
    return sum_of_error


def calc_precision(kms: list, prices: list, t0: float, t1: float) -> float:
    """
    Calculate precision of estimation
    :param kms:
    :param prices:
    :param t0:
    :param t1:
    :return:
    """
    ssr = calc_sum_of_squares_regression(prices, kms, t0, t1)
    sst = calc_sum_of_squares_error(prices)
    return 1 - (ssr / sst)


if __name__ == "__main__":
    thetas_file = get_file_path('..\\data\\thetas.csv')
    data_file = get_file_path('..\\data\\data.csv')

    t0, t1 = get_thetas_from_csv(thetas_file)
    kms, prices = get_data_from_csv(data_file)
    precision = calc_precision(kms, prices, t0, t1)
    print("Precision du programme de regression lineaire: {}".format(precision))
