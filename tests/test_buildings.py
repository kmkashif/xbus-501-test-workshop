# tests.test_buildings
# test module to evaluate the classes in the buildings module
#
# to execute tests, run the following command from project root:
#   nosetests -v --with-coverage --cover-package=motorsports \
#   --cover-inclusive --cover-erase tests
#
# for a list of available asserts:
# https://docs.python.org/2/library/unittest.html#assert-methods
#
# Author:   Allen Leis <allen.leis@georgetown.edu>
# Created:  Fri Sep 11 23:22:32 2015 -0400
#
# Copyright (C) 2015 georgetown.edu
# For license information, see LICENSE.txt
#
# ID: test_buildings.py [] allen.leis@georgetown.edu $

"""
Test cases for buildings module
"""

##########################################################################
## Imports
##########################################################################

import unittest
from unittest import skip
from motorsports.buildings import Garage
from motorsports.buildings import Car

##########################################################################
## Tests
##########################################################################

class GarageTests(unittest.TestCase):

    def test_has_name(self):
        """
        Ensure the garage returns the name provided at creation
        """
        name = 'Bob\'s Garage'
        g = Garage(name)
        self.assertEqual(name, g.name)

#    @skip('pending REST test code')
    def test_allows_cars_to_enter(self):
        """
        Ensure the garage allows Car object to enter
        """
        name = 'Bob\'s Garage'
        g = Garage(name)
        c = Car('black', 'Acura', 'MDX')
        g.enter(c)

#    @skip('pending test code')
    def test_ensure_cars_enter_fully(self):
        """
        Ensure vehicle is in garage after it enters (eg: vehicle in garage == True)
        """
        name = 'Bob\'s Garage'
        g = Garage(name)
        c = Car('black', 'Acura', 'MDX')
        g.enter(c)
        self.assertIn(c, g)

    #@skip('pending test code')
    def test_only_allows_cars_to_enter(self):
        """
        Ensure the garage raises TypeError if non vehicle attempts to enter
        """
        name = 'Bob\'s Garage'
        g = Garage(name)
        c = 12
        with self.assertRaises(TypeError) as cm:
            g.enter(c)

    #@skip('pending test code')
    def test_only_allows_cars_to_exit(self):
        """
        Ensure the garage raises TypeError if non vehicle attempts to exit
        """
        name = 'Bob\'s Garage'
        g = Garage(name)
        c = 12
        with self.assertRaises(TypeError) as cm:
            g.exit(c)

    def test_allows_cars_to_exit(self):
        """
        Ensure vehicles can leave the garage
        """
        name = 'Bob\'s Garage'
        g = Garage(name)
        c = Car('black', 'Acura', 'MDX')
        g.enter(c)
        g.exit(c)

    def test_ensure_cars_exit_fully(self):
        """
        Ensure vehicle is not in garage after it exits
        """
        name = 'Bob\'s Garage'
        g = Garage(name)
        c = Car('black', 'Acura', 'MDX')
        g.enter(c)
        g.exit(c)
        self.assertFalse(c in g)

    #@skip('pending test code')
    def test_raise_lookup_error_on_exit(self):
        """
        Ensure that garage raises LookupError if vehicle attempts
        to exit but was never in garage.
        """
        name = 'Bob\'s Garage'
        g = Garage(name)
        c = Car('black', 'Acura', 'MDX')
        with self.assertRaises(LookupError) as cm:
            g.exit(c)

#    @skip('pending test code')
    def test_iter_builtin(self):
        """
        Ensure we can iterate over garage vehicles by trying to
        iterate over the garage itself
        """
        name = 'Bob\'s Garage'
        g = Garage(name)
        c = Car('black', 'Acura', 'MDX')
        c0 = Car('black', 'Acura', 'TSX')
        g.enter(c)
        g.enter(c0)
        for x in g:
            self.assertIn(x, g)

    #@skip('pending test code')
    def test_len_builtin(self):
        """
        Ensure that the length of the garage matches the number
        of vehicles parked in it
        """
        name = 'Tia\'s Garage'
        g = Garage(name)
        c = Car('black', 'Acura', 'MDX')
        c0 = Car('black', 'Acura', 'TSX')
        g.enter(c)
        g.enter(c0)
        self.assertEquals(6, len(g))
