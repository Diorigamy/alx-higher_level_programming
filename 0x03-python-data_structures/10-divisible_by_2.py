#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    soup = []
    for wat in my_list:
        if wat % 2 == 0:
            soup.append(True)
        else:
            soup.append(False)
    return soup
