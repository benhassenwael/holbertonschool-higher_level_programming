#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        weight = 0
        score = 0
        for w in my_list:
            weight += w[1]
            score += w[0] * w[1]
        return score / weight
    return 0
