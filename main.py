from numerology import chaldean_numerology_values, destiny_numbers
import functools


def destiny_number_calculator():
    print("Welcome to the Numerology Destiny Number Calculator!\n")
    full_name = input("Please enter your full name: ")
    split_name = full_name.split()
    letters = []
    # we work our way down to have individual letters in a list
    for name in split_name:
        for letter in name:
            letters.append(letter.upper())

    values = []
    # convert these individual letters into numbers using chaldean numerology values
    for letter in letters:
        value = 0
        # we check through every key and find which one holds the current letter in our iteration
        for key in list(chaldean_numerology_values.keys()):
            if letter in chaldean_numerology_values[key]:
                value = key
                values.append(value)

    # check len of final number. Split the digits and sum until len == 1 unless it's a master number

    # this functool is similar to JS's Array.reduce()
    final_number = functools.reduce(lambda a, b: a + b, values)
    master_numbers = [11, 22, 33, 44, 55]
    while final_number > 9:
        # Master numbers are okay, we can skip this part
        if final_number in master_numbers:
            break
        # can't split an int, need it to ba a str
        temp = str(final_number)
        new_final = 0
        for num in temp:
            new_final += int(num)
        final_number = new_final

    first_name = full_name.split(" ")[0].capitalize()
    destiny_number_summary = "\n{}, your destiny number is {}.\n\n{}".format(
        first_name, final_number, destiny_numbers[final_number])

    return destiny_number_summary


print(destiny_number_calculator())
