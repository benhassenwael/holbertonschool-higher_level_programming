#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return list(map(lambda elem: replace if elem == search else elem, my_list))
