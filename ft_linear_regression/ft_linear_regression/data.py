import csv
import os


def get_file_path(file: str) -> str:
    """
    Getting file path
    :param file:
    :return: file full path
    """
    return os.path.join(os.path.dirname(__file__), file)


def get_data_from_csv(csv_file: str) -> (list, list):
    """
    Get data from data.csv file
    :param csv_file: data file to extract data
    :return: a tuple of the data
    """
    kms = []
    prices = []
    with open(csv_file, 'r') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        for row in csv_reader:
            kms.append(row[0])
            prices.append(row[1])

    kms.pop(0)
    prices.pop(0)
    for i in range(len(kms)):
        kms[i] = eval(kms[i])
        prices[i] = eval(prices[i])
    return kms, prices


def get_thetas_from_csv(file: str):
    t0, t1 = 0, 0
    if os.path.isfile(file):
        with open(file, 'r') as csv_file:
            file = csv.reader(csv_file, delimiter=',')
            for row in file:
                t0 = float(row[0])
                t1 = float(row[1])
                break
    return t0, t1


def write_theta_data(t0: list, t1: list, file):
    """
    Write theta data into a csv file
    :param t0: theta0 values
    :param t1: theta1 values
    :param file: csv file to write into
    """
    with open(file, 'w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([t0, t1])


def normalize_data(kms: list, prices: list) -> (list, list):
    """
    Normalise the data for the training
    :param kms: km from data.csv
    :param prices: prices from data.csv
    :return: two lists of data normalize
    """
    x = []
    y = []
    km_min = min(kms)
    km_max = max(kms)
    for km in kms:
        x.append((km - km_min) / (km_max - km_min))
    price_min = min(prices)
    price_max = max(prices)
    for price in prices:
        y.append((price - price_min) / (price_max - price_min))
    return x, y


def normalize(data_list: list, elem):
    return (elem - min(data_list)) / (max(data_list) - min(data_list))


def denormalize(data_list: list, elem):
    return (elem * (max(data_list) - min(data_list))) + min(data_list)
