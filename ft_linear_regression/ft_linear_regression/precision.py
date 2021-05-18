from data import get_file_path, get_data_from_csv, get_thetas_from_csv
from ft_linear_regression.ft_linear_regression.lineareg import estimate_price_calc


def calc_precision(kms: list, prices: list, t0: float, t1: float) -> float:
    """
    Calculate precision of estimation
    :param kms:
    :param prices:
    :param t0:
    :param t1:
    :return:
    """
    price_average = sum(prices) / len(prices)
    ssr = sum(map(lambda mileage, price: pow(
        price - estimate_price_calc(mileage, kms, prices, t0, t1), 2
    ), kms, prices))
    sst = sum(map(lambda price: pow(price - price_average, 2), prices))
    return 1 - (ssr / sst)


if __name__ == "__main__":
    thetas_file = get_file_path('thetas.csv')
    data_file = get_file_path('data.csv')

    t0, t1 = get_thetas_from_csv(thetas_file)
    kms, prices = get_data_from_csv(data_file)
    precision = calc_precision(kms, prices, t0, t1)
    print("ft-linear-regression accuracy is: {}".format(precision))
