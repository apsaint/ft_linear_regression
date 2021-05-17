#!/usr/bin/python3

import csv
import os


def estimate_price_calc(kms, th0, th1) -> float:
    """
    Calcul le prix estimé d'une voiture par rapport à son kilometrage
    Parameters
    ----------
    kms: kilometrage

    Returns
    -------
    ep: Prix estimé
    """
    price = float(th0 + (th1 * kms))
    return price


"""
def get_th_from_csv() -> [float, float]:
    file = open("data.csv")
    line = file.readline()
    tab = line.split(",")
    tab[0] = float(tab[0])
    tab[1] = float(tab[1])
    return tab
"""


def main():
    """
    Get the user input for the estimatePrice cal and print the result
    Returns
    -------
    None
    """
    kms = 0
    [theta0, theta1] = [0, 0]
    while kms <= 0:
        kms = input('Saisissez le kilometrage dont vous voulez estimer le prix: ')
        try:
            kms = int(kms)
        except TypeError:
            print('Vous n avez pas saisie une donnée valide. Veuillez entrer un nombre!')
            kms = 0
        if kms < 0:
            print('Un kilometrage ne peut etre < 0!!!')
    p = estimate_price_calc(kms, theta0, theta1)
    print(f'Le prix estimé avec le kilometrage {kms} est de : {p} euros')


if __name__ == "__main__":
    main()
