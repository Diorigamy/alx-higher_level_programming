#!/usr/bin/python3
def remove_char_at(str, n):
    fring = ""
    for i in range(len(str)):
        if i != n:
            fring = fring + str[i]
    return fring
