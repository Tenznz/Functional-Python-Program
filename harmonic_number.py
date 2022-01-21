def display_harmonic_number(number):
    """

    :param number:
    :return:
    """
    i = 2
    harmonic = '1'
    result = 1
    while i <= number:
        harmonic = harmonic + '+1/' + str(i)
        result = result + 1 / i
        i = i+1
    print(harmonic+"=" + str(result))


if __name__ == '__main__':
    input_number = int(input("Enter harmonic number"))
    display_harmonic_number(input_number)
