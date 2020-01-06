# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    entrainement.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: apsaint- <apsaint-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/06 12:20:46 by apsaint-          #+#    #+#              #
#    Updated: 2020/01/06 12:20:46 by apsaint-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/python3

import csv
import os


def estimatePrice_calc(kms, th0, th1) -> float:
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


def read_data(file) -> list:
    """
    Read and return dict
    Parameters
    ----------

    Returns
    -------
    csv_reader
    """
    list_csv = []
    with open(file, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            list_csv.append(row)
    return list_csv


def lr_theta0(csv_reader, theta0, theta1) -> float:

    dth0 = 0.0
    for row in csv_reader:
        dth0 += (theta0 + (theta1 * float(row['km'])) - float(row['price']))
    return float(dth0)


def lr_theta1(csv_reader, theta0, theta1) -> float:
    dth1 = 0.0
    for row in csv_reader:
        dth1 += (theta0 + (theta1 * float(row['km'])) - float(row['price'])) * float(row['km'])
    return float(dth1)


def lr_derivee(csv_reader, theta0, theta1) -> (float, float):
    tmp0 = 0.0
    tmp1 = 0.0
    m = len(csv_reader)
    learningRate = 0.1
    d0 = lr_theta0(csv_reader, theta0, theta1)
    d1 = lr_theta1(csv_reader, theta0, theta1)
    tmp0 = theta0 - (learningRate * (d0 / m))
    tmp1 = theta1 - (learningRate * (d1 / m))
    return (tmp0, tmp1)


def get_max(csv_reader, key) -> float:
    max = 0.0
    for r in csv_reader:
        if float(r[key]) > max:
            max = float(r[key])
    return max


def normalise_data(csv_reader) -> list:
    norm_data = []
    max_km = get_max(csv_reader, 'km')
    max_price = get_max(csv_reader, 'price')
    for row in csv_reader:
        row['km'] = float(row['km']) / max_km
        row['price'] = float(row['price']) / max_price
        norm_data.append(row)
    return norm_data


if __name__ == "__main__":
    csv_reader = read_data('data.csv')
    th = read_data('thetas.csv')
    for row in th:
        th0 = float(row['theta0'])
        th1 = float(row['theta1'])
    norm_data = normalise_data(csv_reader.copy())
    theta0, theta1 = lr_derivee(norm_data, th0, th1)
    theta0 = theta0 * get_max(csv_reader, 'km')
    theta1 = theta1 * (get_max(csv_reader, 'price') / get_max(csv_reader, 'km'))
    p = estimatePrice_calc(240000, theta0, theta1)
    print(p)
