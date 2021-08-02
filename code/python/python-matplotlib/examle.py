# This script produces the image in the slide deck here:
#   https://docs.google.com/presentation/d/1B0FNzR-mzF0FBkRRt0fFITf9DtvRF3XddTPz_qOLCWs/edit#slide=id.g823cb5f81b_0_99

import math
import numpy as np
import matplotlib.pyplot as plt

def main():
    grid = distance_ring(101, 101, 50, 50, 30)
    grid = grid / np.amax(grid) # Normalize
    grid = np.amax(grid) - grid # Inverse
    grid = grid - 0.99 # Shift
    grid = heaviside(9, grid) # Step
    grid = 2 * grid
    heatmap = plt.imshow(grid, cmap='hot', interpolation='nearest', extent=[-120, -119, 52, 53])
    plt.colorbar(heatmap)
    plt.show()
    
    # xs = np.linspace(-10, 10, 100)
    # ys = heaviside(1, xs)
    # plt.plot(xs, ys)
    # plt.show()


def distance_grid(rows, cols, origin_row, origin_col):
    grid = np.zeros((rows, cols))
    for row in range(rows):
        for col in range(cols):
            distance_from_origin = math.sqrt(
                (row - origin_row) * (row - origin_row) +
                (col - origin_col) * (col - origin_col))
            grid[row, col] = distance_from_origin
    return grid

def distance_ring(rows, cols, origin_row, origin_col, radius):
    grid = np.zeros((rows, cols))
    for row in range(rows):
        for col in range(cols):
            distance_from_origin = math.sqrt(
                (row - origin_row) * (row - origin_row) +
                (col - origin_col) * (col - origin_col))
            distance_from_ring = math.sqrt(
                (distance_from_origin - radius) * (distance_from_origin - radius))
            grid[row, col] = distance_from_ring
    return grid

# A smooth approximation of the step function.
# See https://en.wikipedia.org/wiki/Heaviside_step_function
def heaviside(x, k):
    return 1.0 / (1.0 + np.exp(-2 * k * x))

if __name__ == '__main__':
    main()
