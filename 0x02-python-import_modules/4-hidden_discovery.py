#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    for elem in dir(hidden_4):
        if elem[0] != '_':
            print(elem)
