#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    Int_Max = my_list[0]
    for item in my_list:
        if item > Int_Max:
            Int_Max = item
    return Int_Max
