#!/usr/bin/python3
import csv
import os
import sys

from ft_linear_regression.ft_linear_regression.data import normalize, denormalize, get_file_path, get_data_from_csv, \
    get_thetas_from_csv


def estimate_price_calc(kms: list, prices: list, input_kms: int, th0: float, th1: float) -> float:
    """
    Calculate the estimate price with equation and data normalisation
    :param kms: kms data
    :param prices: prices from data
    :param input_kms: input kms from user
    :param th0: theta 0 value
    :param th1: theta 1 value
    :return: price
    """
    normalise_kms = normalize(kms, input_kms)
    normalize_price = float(th0 + (th1 * normalise_kms))
    price = denormalize(prices, normalize_price)
    return price


def get_user_km() -> int:
    """
    Get the user input for the estimatePrice cal and print the result
    Returns input_kms in int
    -------
    None
    """
    input_kms = 0
    while input_kms <= 0:
        try:
            input_kms = input('Saisissez le kilometrage dont vous voulez estimer le prix: ')
            input_kms = int(input_kms)
        except EOFError:
            sys.exit('EOF. Exit...')
        except TypeError:
            print('Vous n avez pas saisie une donnée valide. Veuillez entrer un nombre!')
            input_kms = 0
        if input_kms < 0:
            print('Un kilometrage ne peut etre < 0!!!')
    return input_kms


if __name__ == "__main__":
    """
    Main function for estimation program
    """
    thetas_file = get_file_path('..\\data\\thetas.csv')
    data_file = get_file_path('..\\data\\data.csv')

    t0, t1 = get_thetas_from_csv(thetas_file)
    input_kms = get_user_km()
    kms, prices = get_data_from_csv(data_file)
    price = estimate_price_calc(kms, prices, input_kms, t0, t1)
    if price < 0:
        price = "{} prix negatif?! Probleme ou pas une bonne affaire".format(price)
    print('Le prix estime pour ce kilometrage est de: {}'.format(price))
