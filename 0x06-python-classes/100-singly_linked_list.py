#!/usr/bin/python3
""" Singly linked list in Python """


class Node:
    """Class to represent node of singly linked list"""
    def __init__(self, data, next_node=None):
        if type(data) is int:
            self.__data = data
        else:
            raise TypeError("data must be integer")
        if (next_node is not None and
           type(next_node) is not Node):
                raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is int:
            self.__data = vlaue
        else:
            raise TypeError("data must be integer")

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if (value is not None and
           type(value) is not Node):
                raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """Class to store singly linked list of Node objects"""
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """ sorted insert into ascending linked list"""
        node = Node(value)
        if self.__head is None:
            self.__head = node
        elif value <= self.__head.data:
            node.next_node = self.__head
            self.__head = node
        else:
            looper = self.__head
            while (looper.next_node is not None and
                    looper.next_node.data < value):
                looper = looper.next_node
            node.next_node = looper.next_node
            looper.next_node = node

    def __str__(self):
        s = ""
        looper = self.__head
        while looper.next_node:
            s += "{}\n".format(looper.data)
            looper = looper.next_node
        s += "{}".format(looper.data)
        return s
