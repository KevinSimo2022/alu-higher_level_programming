#!/usr/bin/python3
"""Defines a matrix multiplication function"""


def matrix_mul(m_a, m_b):
    """Multiply two matrices by each other if possible.

    Args:
        m_a: The first matrix
        m_b: The second matrix

    Returns:
        A new matrix representing the multiplication of m_a by m_b.

    Raises:
        TypeError: If either m_a or m_b is not a list of list of ints/floats
        ValueError: If either m_a or m_b is empty.
        TypeError: If either m_a or m_b has different-sized rows
        ValueError: If m_a and m_b cannot be multiplied
        TypeError: If m_a should contain only integers or floats
        TypeError: If m_b should contain only integers or floats
    """
    # Validate input matrices
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    if not all(isinstance(num, (int, float)) for row in m_a for num in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(num, (int, float)) for row in m_b for num in row):
        raise TypeError("m_b should contain only integers or floats")
    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Compute the product of the two matrices
    result = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            value = sum(m_a[i][k] * m_b[k][j] for k in range(len(m_b)))
            row.append(value)
        result.append(row)

    return result
