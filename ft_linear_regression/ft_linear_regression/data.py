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


