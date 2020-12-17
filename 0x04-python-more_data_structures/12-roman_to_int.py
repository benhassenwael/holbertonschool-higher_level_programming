#!/usr/bin/python3
def roman_to_int(roman_string):
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
    for i in range(len(roman_string)):
        c = roman_string[i]
        next_c = roman_string[i + 1] if i < len(roman_string) - 1 else None
        if c not in num_val:
            return 0
        if next_c and num_val[c] < num_val[next_c]:
                sum -= num_val[roman_string[i]]
        else:
            sum += num_val[roman_string[i]]
    return sum
