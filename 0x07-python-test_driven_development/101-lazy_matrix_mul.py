#!/usr/bin/python3
""" Introduction to NumPy """
import numpy


def lazy_matrix_mul(m_a, m_b):
    """ Multiply 2 matrices using NumPy

        Args:
            m_a: list of lists of integers or floats
            m_b: list of lists of integers or floats

        Returns:
            the resulting matrix
    """
    return numpy.matmul(m_a, m_b)
