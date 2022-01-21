import random


def flip_coin():
    """

    :return:
    """
    coin = [0, 1]
    if random.choice(coin) == 0:
        print("head")
    else:
        print("tail")


if __name__ == '__main__':
    flip_coin()
