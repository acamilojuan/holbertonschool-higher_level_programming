#!/usr/bin/python3
"""Function that finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Mehod to find the peak"""
    if len(list_of_integers) > 0:
        sort(list_of_integers)
        return list_of_integers[-1]
    else:
        return None
