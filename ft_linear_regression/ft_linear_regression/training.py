#!/usr/bin/python3

import csv
import os

from ft_linear_regression.ft_linear_regression.data import get_file_path


def estimate_price(kms, th0, th1) -> float:
    """
    Calcul le prix estimé d'une voiture par r   apport à son kilometrage
    Parameters
    ----------
    kms: kilometrage
    th0:
    th1:

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
    learning_rate = 0.1
    d0 = lr_theta0(csv_reader, theta0, theta1)
    d1 = lr_theta1(csv_reader, theta0, theta1)
    tmp0 = theta0 - (learning_rate * (d0 / m))
    tmp1 = theta1 - (learning_rate * (d1 / m))
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


def gradient_descent(kms: list, prices: list):
    """
    Gradient descent with learning rate
    :param kms:
    :param prices:
    :return:
    """
    learning_rate = 0.5
    iterations = 100

    loss_history = []
    t0_history = [0.0]
    t1_history = [0.0]
    t0 = 0.0
    t1 = 0.0
    message = "max epoch reached"

    for iteration in range(iterations):
        dt0 = 0
        dt1 = 0
        for mileage, price in zip(kms, prices):
            dt0 += (t1 * mileage + t0) - price
            dt1 += ((t1 * mileage + t0) - price) * mileage
        t0 -= dt0 / len(kms) * learning_rate
        t1 -= dt1 / len(prices) * learning_rate
        loss = lossFunction(t0, t1, kms, prices)
        if iteration % 10 == 0:
            print("epoch {} - loss: {:.8}".format(iteration, loss))
        t0, t1, learning_rate = boldDriver(loss, loss_history, t0, t1, dt0, dt1, learning_rate, len(kms))
        loss_history.append(loss)
        t0_history.append(t0)
        t1_history.append(t1)
        if earlyStopping(loss_history):
            message = "early stopped"
            break
    print("\nend: {}.".format(message))
    print("epoch {} - loss: {:.8}".format(iteration, loss))
    return (t0, t1, loss_history, t0_history, t1_history)


if __name__ == "__main__":
    data_file = get_file_path('data.csv')
    csv_reader = read_data(data_file)
    th = read_data('thetas.csv')
    for row in th:
        th0 = float(row['theta0'])
        th1 = float(row['theta1'])
    norm_data = normalise_data(csv_reader.copy())
    theta0, theta1 = lr_derivee(norm_data, th0, th1)
    theta0 = theta0 * get_max(csv_reader, 'km')
    theta1 = theta1 * (get_max(csv_reader, 'price') / get_max(csv_reader, 'km'))
    p = estimate_price_calc(240000, theta0, theta1)
    print(p)
