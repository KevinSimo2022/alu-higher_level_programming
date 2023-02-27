#!/usr/bin/python3
def no_c(my_string):
    new_S = my_string.translate({ord('c'): None})
    new_S = new_S.translate({ord('C'): None})
    return new_s
