#!/usr/bin/python3
def roman_to_int(roman_string):
        return 0
    romans = {'I': 1, 'V': 5, 'X': 10, 'L':50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
    num = 0
    num_list = list()
    if len(roman_string) == 1:
        return roman_numerals[roman_string]
    if len(roman_string) > 1:
        for i in range(0, len(roman_string)):
            try:
                if roman_string[i] == "I" and \
                        (roman_string[i + 1] == "V" or
                         roman_string[i + 1] == "X") \
                        or roman_string[i] == "X" and \
                        (roman_string[i + 1] == "C" or
                         roman_string[i + 1] == "L") \
                        or roman_string[i] == "C" and \
                        (roman_string[i + 1] == "D" or
                         roman_string[i + 1] == "M"):
                    num_list.append(-int(roman_numerals[roman_string[i]]))
                else:
                    num_list.append(int(roman_numerals[roman_string[i]]))
            except IndexError:
                num_list.append(int(roman_numerals[roman_string[i]]))
                pass
    return sum(num_list)
