def power_of_two(power):
    """

    :param power:
    :return:
    """
    i = 1
    res = 1
    while i <= power:
        res = res * 2
        i = i + 1
    print(res)


if __name__ == '__main__':
    number_input = int(input("Enter power of 2: "))
    power_of_two(number_input)