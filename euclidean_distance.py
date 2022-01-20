import math


def euclidean_distance(x_axis, y_axis):
    """

    :param x_axis:
    :param y_axis:
    :return:
    """
    print("Euclidean Distance:", math.pow(x_axis * x_axis + y_axis * y_axis, 0.5))


if __name__ == '__main__':
    print("Euclidean distance from origin (0,0)")
    x_input = int(input("Enter x-axis:"))
    y_input = int(input("Enter y-axis:"))
    euclidean_distance(x_input, y_input)
