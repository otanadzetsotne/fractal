import random as rd
from math import sin, cos, radians

import numpy as np
from matplotlib import pyplot as plt


def get_rnd(scale: int):
    return rd.random() * scale


def get_middle(a: np.array, b: np.array):
    x = (a[0] + b[0]) / 2
    y = (a[1] + b[1]) / 2
    return np.array([x, y])


def get_figure(angles: int, scale: int, symmetry: bool):
    return get_figure_right(angles=angles, scale=scale) if symmetry else get_figure_random(angles=angles, scale=scale)


def get_figure_right(angles: int, scale: int):
    figure = [[0, scale / 2], [0, 0]]

    a = np.array([figure[0][0], figure[1][0]])
    b = np.array([figure[0][1], figure[1][1]])

    length = ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** .5
    angle_step = 180 - ((180 * (angles - 2)) / angles)
    angle = angle_step
    last_dot = np.array([figure[0][1], figure[1][1]])
    for i in range(angles - 1):
        x = (length * cos(radians(angle))) + last_dot[0]
        y = (length * sin(radians(angle))) + last_dot[1]
        last_dot = np.array([x, y])

        figure[0].append(x)
        figure[1].append(y)

        angle += angle_step

    return np.array(figure)


def get_figure_random(angles: int, scale: int):
    xs = [get_rnd(scale) for i in range(angles)]
    ys = [get_rnd(scale) for i in range(angles)]
    return np.array([xs, ys])


def fractal_dots(
        angles: int = 3,
        symmetry: bool = True,
        iterations: int = 10000,
        update: int = 100,
        scale: int = 1000,
        dot_size: float = .1,
        color: str = 'black'):

    def draw_figure(f: np.array, c: str, s: float):
        plt.scatter(f[0], f[1], c=c, s=s)
        plt.draw()
        plt.gcf().canvas.flush_events()

    plt.ion()
    plt.show()

    figure = get_figure(angles, scale, symmetry)
    draw_figure(f=figure, c=color, s=dot_size)

    loc = np.array([get_rnd(scale), get_rnd(scale)])
    draw_figure(f=loc, c=color, s=dot_size)

    xs = np.array([loc[0]])
    ys = np.array([loc[1]])
    for i in range(iterations):
        rnd = rd.randint(0, angles - 1)
        target = np.array([figure[0][rnd], figure[1][rnd]])

        loc = get_middle(loc, target)

        xs = np.insert(xs, 0, loc[0])
        ys = np.insert(ys, 0, loc[1])

        if i % update == 0:
            draw_figure(f=np.array(xs, ys), c=color, s=dot_size)
            xs = np.array([loc[0]])
            ys = np.array([loc[1]])

    plt.ioff()
    plt.show()
    return True
