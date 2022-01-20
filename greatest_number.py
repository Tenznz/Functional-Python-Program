def greatest_number(num1, num2, num3):
    """

    :param num1:
    :param num2:
    :param num3:
    :return:
    """
    if num1 > num2 or num1 > num3:
        return num1
    elif num2 > num3:
        return num2
    else:
        return num3


if __name__ == '__main__':
    input_num1 = int(input("Enter 1st number:"))
    input_num2 = int(input("Enter 2nd number:"))
    input_num3 = int(input("Enter 3rd number:"))

    print(greatest_number(input_num1, input_num2, input_num3), "is greatest")
    