import math

import numpy as np
from matplotlib import pyplot as plt


def get_middle(a: np.array, b: np.array, scale: float = 0.5):
    x = a[0] + (b[0] - a[0]) * scale
    y = a[1] + (b[1] - a[1]) * scale
    return np.array([x, y])


def get_figure(angles: int, scale: int):
    figure = [[0, scale / 2], [0, 0]]

    a = np.array([figure[0][0], figure[1][0]])
    b = np.array([figure[0][1], figure[1][1]])

    length = ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** .5
    angle_step = 180 - ((180 * (angles - 2)) / angles)
    angle = angle_step
    last_dot = np.array([figure[0][1], figure[1][1]])
    for i in range(angles - 1):
        x = (length * math.cos(math.radians(angle))) + last_dot[0]
        y = (length * math.sin(math.radians(angle))) + last_dot[1]
        last_dot = np.array([x, y])

        figure[0].append(x)
        figure[1].append(y)

        angle += angle_step

    return np.array(figure)


def fractal_cokh(
        iterations: int = 5,
        angles: int = 3,
        scale: int = 1000,
        color: str = 'black',
        update: int = 1000,
        outer: bool = True,
        incline: float = 1.0):

    def draw_figure(f: np.array, c: str, w: int = 1):
        plt.plot(f[0], f[1], color=c, linewidth=w)
        plt.draw()
        plt.gcf().canvas.flush_events()

    figure = get_figure(angles, scale)
    xs = list(figure[0])
    ys = list(figure[1])

    draw_figure(f=figure, c=color)
    cos = 0.5 * incline
    sin = 0.866 * (-1 if outer else 1) * incline

    plt.ion()
    plt.show()

    counter = 1
    for i in range(iterations):
        for j in range(len(xs) - 1):
            a = np.array([figure[0][j], figure[1][j]])
            b = np.array([figure[0][j + 1], figure[1][j + 1]])

            left = get_middle(a, b, 1/3)
            right = get_middle(a, b, 2/3)

            new_x = left[0] + (right[0] - left[0]) * cos - sin * (right[1] - left[1])
            new_y = left[1] + (right[0] - left[0]) * sin + cos * (right[1] - left[1])

            loc = j + 1 + (3 * j)
            xs = xs[:loc] + [left[0]] + [new_x] + [right[0]] + xs[loc:]
            ys = ys[:loc] + [left[1]] + [new_y] + [right[1]] + ys[loc:]

            if counter % update == 0:
                draw_figure(f=np.array([xs, ys]), c=color)
            counter += 1

        figure = np.array([xs, ys])
        
    draw_figure(f=figure, c=color)

    plt.ioff()
    plt.show()
    return True
