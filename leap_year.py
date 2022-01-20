def check_leap(year):
    """

    :param year:
    :return:
    """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(year, "is leap year")
            else:
                print(year, "is not leap year")
        else:
            print(year, "is leap year")
    else:
        print(year, "Not a leap year")


if __name__ == "__main__":
    input_year = int(input("Enter the year"))
    check_leap(input_year)
    