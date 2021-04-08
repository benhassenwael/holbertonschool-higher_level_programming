#!/usr/bin/python3
""" defenition of find_peak function """


def find_peak(list_of_integers):
    if not list_of_integers:
        return None
    li = list_of_integers
    start = 0
    end = len(li) - 1
    while (start < end):
        mid = start + ((end - start) // 2)
        if (li[mid - 1] < li[mid] and li[mid + 1] < li[mid]):
            return li[mid]
        elif (li[mid - 1] > li[mid + 1]):
            end = mid
        else:
            start = mid + 1
    return li[start]

