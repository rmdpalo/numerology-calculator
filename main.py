from numerology import chaldean_numerology_values
import functools

# print(chaldean_numerology_values)


def name_calculator():
    name = input("What is your FULL name?: ")
    split_name = name.split()
    letters = []
    # we work our way down to have individual letters in a list
    for name in split_name:
        for letter in name:
            letters.append(letter.upper())

    values = []
    # convert these individual letters into numbers using chaldean numerology values
    for letter in letters:
        value = 0
        for key in list(chaldean_numerology_values.keys()):
            if letter in chaldean_numerology_values[key]:
                value = key
                values.append(value)

    # add all values together
    # check len of final number. Split the digits and sum until len == 1
    final_number = functools.reduce(lambda a, b: a + b, values)
    # print("before loop", final_number)
    while final_number > 9:
        temp = str(final_number)
        temp_list = temp.split()
        new_final = 0
        for num in temp:
            new_final += int(num)
        final_number = new_final
        # print("temp", temp)
        # print("temp list", temp_list)
        # print("new_final", new_final)
        # print("final_number", final_number)

    return final_number


print(name_calculator())
