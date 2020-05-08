#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    for score in a_dictionary:
        return max(a_dictionary, key=a_dictionary.get)
