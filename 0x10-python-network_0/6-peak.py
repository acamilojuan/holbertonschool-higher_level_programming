#!/usr/bin/python3
"""Function that finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Mehod to find the peak"""
    if len(list_of_integers) > 0:
        return max(list_of_integers)
    else:
        return None
