#!/usr/bin/python3
""" This module contains a single function
    for the purpose of practecing doctests """


def matrix_mul(m_a, m_b):
    """ Multiply 2 matrices

    Args:
        m_a: list of lists of integers or floats
        m_b: list of lists of integers or floats

    Returns:
        the resulting matrix

    Raises:
        TypeError: if any of the matrices is not valid
        ValueError: if the matrices can't be multiplied
    """
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    if not m_a or not any(m_a):
        raise ValueError("m_a can't be empty")
    if not m_b or not any(m_b):
        raise ValueError("m_b can't be empty")
    for row in m_a:
        if type(row) is not list:
            raise TypeError("m_a must be list of lists")
    for row in m_b:
        if type(row) is not list:
            raise TypeError("m_b must be list of lists")
    for row in m_a:
        if any(map(lambda el: (
                    type(el) is not int and type(el) is not float), row)):
            raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        if any(map(lambda el: (
                    type(el) is not int and type(el) is not float), row)):
            raise TypeError("m_b should contain only integers or floats")
    len_a = len(m_a[0])
    for row in m_a:
        if len(row) != len_a:
            raise TypeError("each row of m_a must be of the same size")
    len_b = len(m_b[0])
    for row in m_b:
        if len(row) != len_b:
            raise TypeError("each row of m_b must be of the same size")
    if len_a != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    m_res = []
    for i in range(len(m_a)):
        res_row = []
        for j in range(len_b):
            cell_prod = 0
            for k in range(len_a):
                cell_prod += m_a[i][k] * m_b[k][j]
            res_row.append(cell_prod)
        m_res.append(res_row)
    return m_res
