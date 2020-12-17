#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str:
        return 0
    num_val = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1
            }
    sum = 0
    roman_num = [num_val[c] if c in num_val else 0 for c in roman_string]
    for i in range(len(roman_num)):
        if roman_num[i] == 0:
            return 0
        if i < len(roman_num) - 1 and roman_num[i] < roman_num[i + 1]:
            sum -= roman_num[i]
        else:
            sum += roman_num[i]
    return sum
