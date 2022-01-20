def check_even(number):
    """

    :param number:
    :return:
    """
    if number % 2 == 0:
        return 'even'
    else:
        return 'odd'


if __name__ == '__main__':
    input_number = int(input("Enter a number"))
    print(check_even(input_number))
