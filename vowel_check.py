def vowel_check(letter):
    """

    :param letter:
    :return:
    """
    letter = letter.lower()
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
        print("Vowel letter")
    else:
        print("Consonant letter")


if __name__ == '__main__':
    input_letter = str(input("Enter letter"))
    vowel_check(input_letter)