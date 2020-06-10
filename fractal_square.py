from matplotlib import pyplot as plt
import matplotlib.patches as patches
import numpy as np


def fractal_square(depth: int = 2, size: int = 500):

    def run_recursion(ax, dot: np.array, width: float, max_depth: int, current_depth: int = 0):
        if current_depth == max_depth:
            return
        current_depth += 1

        x = dot[0]
        y = dot[1]
        half_size = width / 2
        third_size = width / 3

        ax.add_patch(patches.Rectangle(
            (x - half_size, y - half_size),  # (x,y)
            width,  # width
            width,  # height
            color='black'
        ))

        ax.add_patch(patches.Rectangle(
            (x - (third_size / 2), y - (third_size / 2)),  # (x,y)
            third_size,  # width
            third_size,  # height
            color='white'
        ))

        new_dots = np.array([
            [x - third_size, y + third_size],
            [x, y + third_size],
            [x + third_size, y + third_size],
            [x + third_size, y],
            [x + third_size, y - third_size],
            [x, y - third_size],
            [x - third_size, y - third_size],
            [x - third_size, y],
        ])

        for i in range(len(new_dots)):
            run_recursion(ax, new_dots[i], third_size, max_depth, current_depth)

        plt.draw()
        plt.gcf().canvas.flush_events()

    def main(max_rec_depth: int, max_width: int):
        fig1 = plt.figure()
        ax = fig1.add_subplot(111, aspect='equal')
        ax.axis([-max_width, max_width, -max_width, max_width])

        fig_manager = plt.get_current_fig_manager()
        fig_manager.window.showMaximized()
        plt.ion()
        plt.show()

        run_recursion(ax, np.array([0, 0]), max_width, max_rec_depth)

        plt.ioff()
        plt.show()

    main(depth, size)
