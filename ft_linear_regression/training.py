#!/usr/bin/python3

import csv
import os

from ft_linear_regression.data import get_file_path, get_data_from_csv, get_thetas_from_csv, \
    normalize_data, write_theta_data
from ft_linear_regression.visualiser import display


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
        dt0, dt1 = derivate(kms, prices, t0, t1)
        t0 -= dt0 / len(kms) * learning_rate
        t1 -= dt1 / len(prices) * learning_rate
        loss = cost(t0, t1, kms, prices)
        if iteration % 10 == 0:
            print("epoch {} - loss: {:.8}".format(iteration, loss))
        t0, t1, learning_rate = bold_driver(loss, loss_history, t0, t1, dt0, dt1, learning_rate, len(kms))
        loss_history.append(loss)
        t0_history.append(t0)
        t1_history.append(t1)
        if early_stopping(loss_history):
            message = "early stopped"
            break
    print("\nend: {}.".format(message))
    print("epoch {} - loss: {:.8}".format(iteration, loss))
    return t0, t1, loss_history, t0_history, t1_history


def derivate(kms, prices, t0, t1):
    """

    :param kms:
    :param prices:
    :param t0:
    :param t1:
    :return:
    """
    dt0 = 0
    dt1 = 0
    for mileage, price in zip(kms, prices):
        dt0 += (t1 * mileage + t0) - price
        dt1 += ((t1 * mileage + t0) - price) * mileage
    return dt0, dt1


def cost(t0, t1, mileages, prices):
    """
    Calculate cost for derivative

    :param t0:
    :param t1:
    :param mileages:
    :param prices:
    :return:
    """
    loss = 0.0
    for mileage, price in zip(mileages, prices):
        loss += (price - (t1 * mileage + t0)) ** 2
    return loss / len(mileages)


def bold_driver(loss, loss_history, t0, t1, dt0, dt1, learning_rate, length):
    """
    Update model parameters (learning rate)
    :param loss:
    :param loss_history:
    :param t0:
    :param t1:
    :param dt0:
    :param dt1:
    :param learning_rate:
    :param length:
    :return:
    """
    newlearning_rate = learning_rate
    if len(loss_history) > 1:
        if loss >= loss_history[-1]:
            t0 += dt0 / length * learning_rate
            t1 += dt1 / length * learning_rate
            newlearning_rate *= 0.5
        else:
            newlearning_rate *= 1.05
    return t0, t1, newlearning_rate


def early_stopping(loss_history) -> bool:
    """
    Stop the training when the loss start to grow
    :param loss_history: measure the poorness of the model
    :return: True if stopping is necessary or False
    """
    check = 8
    if len(loss_history) > check:
        mean = sum(loss_history[-(check):]) / check
        last = loss_history[-1]
        if round(mean, 9) == round(last, 9):
            return True
    return False


if __name__ == "__main__":
    # Data recuperation
    data_file = get_file_path('.\\data\\data.csv')
    thetas_file = get_file_path('.\\data\\thetas.csv')
    kms, prices = get_data_from_csv(data_file)

    x, y = normalize_data(kms, prices)
    t0, t1, loss_history, t0_history, t1_history = gradient_descent(x, y)
    write_theta_data(t0, t1, thetas_file)
    display(t0, t1, kms, prices, loss_history, t0_history, t1_history)

