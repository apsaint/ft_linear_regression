import matplotlib.pyplot as plt

from ft_linear_regression.data import denormalize, normalize


def visual_linear_regression(kms, prices, t0, t1):
    """
    Representation of the training model regression
    :param kms:
    :param prices:
    """
    lineX = [float(min(kms)), float(max(kms))]
    lineY = []
    for elem in lineX:
        elem = t1 * normalize(kms, elem) + t0
        lineY.append(denormalize(prices, elem))
    f1 = plt.figure(1)
    f1.canvas.manager.set_window_title('Linear regression')
    plt.plot(kms, prices, 'bo', lineX, lineY, 'r-')
    plt.xlabel('km')
    plt.ylabel('prix')


def visual_cost(loss_history):
    """

    :param loss_history:
    """
    f2 = plt.figure(2)
    f2.canvas.manager.set_window_title('Perte')
    plt.plot(loss_history, 'r.')
    plt.xlabel('iterations')
    plt.ylabel('perte')


def visual_thetas(t0_history, t1_history):
    """

    :param loss_history:
    """
    # t0 history visual
    f3 = plt.figure(3)
    f3.canvas.manager.set_window_title('t0 evolution')
    plt.plot(t0_history, 'g.')
    plt.xlabel('iterations')
    plt.ylabel('t0')

    # t1 history visual
    f4 = plt.figure(4)
    f4.canvas.manager.set_window_title('t1 evolution')
    plt.plot(t1_history, 'b.')
    plt.xlabel('iterations')
    plt.ylabel('t1')


def display(t0, t1, kms, prices, loss_history, t0_history, t1_history):
    """
    Display training visualisations
    :param t0:
    :param t1:
    :param kms:
    :param prices:
    :param loss_history:
    :param t0_history:
    :param t1_history:
    """
    visual_linear_regression(kms, prices, t0, t1)
    visual_cost(loss_history)
    visual_thetas(t0_history, t1_history)
    plt.show()
