from matplotlib import pyplot as plt
import random as rd
import numpy as np


def get_rnd(scale: int):
    return rd.random() * scale


def get_middle(a: np.array, b: np.array):
    x = (a[0] + b[0]) / 2
    y = (a[1] + b[1]) / 2
    return np.array([x, y])


def draw_triangle(
        iterations: int = 10000,
        update: int = 100,
        scale: int = 1000,
        dot_size: float = .1,
        color: str = 'black'
):
    plt.title("Triangle fractal")  # заголовок

    a = np.array([get_rnd(scale), get_rnd(scale)])
    plt.scatter(a[0], a[1], c=color, s=dot_size)

    b = np.array([get_rnd(scale), get_rnd(scale)])
    plt.scatter(b[0], b[1], c=color, s=dot_size)

    c = np.array([get_rnd(scale), get_rnd(scale)])
    plt.scatter(c[0], c[1], c=color, s=dot_size)

    loc = np.array([get_rnd(scale), get_rnd(scale)])
    plt.scatter(loc[0], loc[1], c=color, s=dot_size)

    fig_manager = plt.get_current_fig_manager()
    fig_manager.window.showMaximized()

    plt.ion()

    xs = np.array([loc[0]])
    ys = np.array([loc[1]])
    for i in range(iterations):
        rnd = rd.randint(0, 3)
        if rnd == 0:
            target = a
        elif rnd == 1:
            target = b
        else:
            target = c

        mid = get_middle(loc, target)
        loc = mid

        xs = np.insert(xs, 0, loc[0])
        ys = np.insert(ys, 0, loc[1])

        if i % update == 0:
            plt.scatter(xs, ys, c=color, s=dot_size)
            plt.draw()
            plt.gcf().canvas.flush_events()
            xs = np.array([loc[0]])
            ys = np.array([loc[1]])
            print(i)

    plt.ioff()
    plt.show()
