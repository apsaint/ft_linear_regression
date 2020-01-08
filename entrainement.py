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


def partial_derivative(csv_reader, theta0, theta1, m) -> (float, float):
    dth0 = 0.0
    dth1 = 0.0
    for row in csv_reader:
        dth0 += (theta0 + (theta1 * float(row['km'])) - float(row['price']))
        dth1 += (theta0 + (theta1 * float(row['km'])) - float(row['price'])) * float(row['km'])
    dth0 = (1.0/m) * dth0
    dth1 = (1.0/m) * dth1
    return (float(dth0), float(dth1))


def calc_new_thetas(csv_reader, theta0, theta1) -> (float, float):
    m = len(csv_reader)
    learningRate = 0.1
    (d0, d1) = partial_derivative(csv_reader, theta0, theta1, m)
    new_theta0 = theta0 - (learningRate * d0)
    new_theta1 = theta1 - (learningRate * d1)
    return (new_theta0, new_theta1)


def start_gradient_descent(csv_reader, theta0, theta1) -> (float, float):
    tmpth0 = theta0
    tmpth1 = theta1
    for r in csv_reader:
        new_theta0, new_theta1 = calc_new_thetas(csv_reader, tmpth0, tmpth1)
        tmpth0, tmpth1 = new_theta0, new_theta1
    return ((tmpth0, tmpth1))


def get_max(csv_reader, key) -> float:
    max = 0.0
    for r in csv_reader:
        if float(r[key]) > max:
            max = float(r[key])
    return max


def get_min(csv_reader, key) -> float:
    min = 123456.0
    for r in csv_reader:
        if float(r[key]) < min:
            min = float(r[key])
    return min


def normalise_data(csv_reader) -> list:
    norm_data = []
    max_km = get_max(csv_reader, 'km')
    min_km = get_min(csv_reader, 'km')
    max_price = get_max(csv_reader, 'price')
    min_price = get_min(csv_reader, 'price')
    for row in csv_reader:
        row['km'] = (float(row['km']) - min_km) / (max_km - min_km)
        row['price'] = (float(row['price']) - min_price) / (max_price - min_price)
        norm_data.append(row)
    return norm_data


if __name__ == "__main__":
    csv_reader = read_data('data.csv')
    th = read_data('thetas.csv')
    for row in th:
        th0 = float(row['theta0'])
        th1 = float(row['theta1'])
    #norm_data = normalise_data(csv_reader.copy())
    theta0, theta1 = start_gradient_descent(csv_reader, th0, th1)
    p = estimatePrice_calc(240000, theta0, theta1)
    print(p)
