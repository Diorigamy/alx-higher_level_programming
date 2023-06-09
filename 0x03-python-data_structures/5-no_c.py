#!/usr/bin/python3
def no_c(my_string):
    strn = ""
    for i in my_string:
        if i not in ["c", "C"]:
            strn = strn + i
    return strn
