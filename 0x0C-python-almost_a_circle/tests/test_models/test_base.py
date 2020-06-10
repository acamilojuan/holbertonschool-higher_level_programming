#!/usr/bin/python3


"""Importing modules and classes needed to test
Definition of cases
"""
import unittest
import pep8
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestsBase(unittest.TestCase):
    """Class to test the Base cases"""
    def setUp(self):
        """Setup method"""
        Base._Base__nb_objects = 0

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/base.py'])
        self.assertEqual(result.total_errors, 0)
