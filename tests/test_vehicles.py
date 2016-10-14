# tests.test_vehicles
# test module to evaluate the classes in the vehicles module
#
# for a list of available asserts:
# https://docs.python.org/2/library/unittest.html#assert-methods
#
# to execute tests, run the following command from project root:
#   nosetests -v --with-coverage --cover-package=motorsports \
#   --cover-inclusive --cover-erase tests
#
# Author:   Allen Leis <allen.leis@georgetown.edu>
# Created:  Fri Sep 11 23:22:32 2015 -0400
#
# Copyright (C) 2015 georgetown.edu
# For license information, see LICENSE.txt
#
# ID: test_vehicles.py [] allen.leis@georgetown.edu $

"""
Test cases for vehicles module
"""

##########################################################################
## Imports
##########################################################################

import unittest
from unittest import skip
from motorsports.buildings import Car, BaseVehicle

##########################################################################
## Tests
##########################################################################

class VehicleTests(unittest.TestCase):

    #@skip('pending test code')
    def test_description(self):
        """
        Ensure the car description return a string of: "color, make model"
        """
        clr = 'black'
        m1 = 'Acura'
        m2 = 'MDX'
        c = Car(clr, m1, m2)
        self.assertEquals(c.description, '{} {} {}'.format(clr, m1, m2))

    #@skip('pending test code')
    def test_initial_state_is_stopped(self):
        """
        Ensure the a car's initial state is "stopped"
        """
        clr = 'black'
        m1 = 'Acura'
        m2 = 'MDX'
        c = Car(clr, m1, m2)
        self.assertEquals('stopped', c.state)

    #@skip('pending test code')
    def test_state_after_start(self):
        """
        Ensure the car's state is "started" after using start method
        """
        clr = 'black'
        m1 = 'Acura'
        m2 = 'MDX'
        c = Car(clr, m1, m2)
        c.start()
        self.assertEquals('started', c.state)

    #@skip('pending test code')
    def test_state_after_stop(self):
        """
        Ensure the car's state is "stopped" after using shutdown method
        """
        clr = 'black'
        m1 = 'Acura'
        m2 = 'MDX'
        c = Car(clr, m1, m2)
        c.start()
        c.shutdown()
        self.assertEquals('stopped', c.state)

    #@skip('pending test code')
    def test_str_builtin(self):
        """
        Ensure the car evaluates to a string of
        "I am a <car color>, <car make>, <car model>."
        """
        clr = 'black'
        m1 = 'Acura'
        m2 = 'MDX'
        c = Car(clr, m1, m2)
        self.assertEquals(str(c), 'I am a {} {} {}.'.format(clr, m1, m2))

    #@skip('pending test code')
    def test_color_requirement(self):
        """
        Ensure the car requires a color argument during instantiation
        """
        m1 = 'Acura'
        m2 = 'MDX'
        with self.assertRaises(TypeError) as cm:
            c = Car(make=m1, model=m2)

    #@skip('pending test code')
    def test_make_requirement(self):
        """
        Ensure the car requires a make argument during instantiation
        """
        clr = 'black'
        m2 = 'MDX'
        with self.assertRaises(TypeError) as cm:
            c = Car(color=clr, model=m2)

    #@skip('pending test code')
    def test_model_requirement(self):
        """
        Ensure the car requires a model argument during instantiation
        """
        clr = 'black'
        m1 = 'Acura'
        with self.assertRaises(TypeError) as cm:
            c = Car(make=m1, color=clr)

    #@skip('pending test code')
    def test_state_read_only(self):
        """
        Ensure the car state attribute is read only and throws
        AttributeError if someone tries to assign a value directly
        """
        clr = 'black'
        m1 = 'Acura'
        m2 = 'MDX'
        c = Car(clr, m1, m2)
        with self.assertRaises(AttributeError) as cm:
            c.state = 'string'

    #@skip('pending test code')
    def test_car_is_a_vehicle(self):
        """
        Ensure a car object is also an instance of BaseVehicle
        """
        c = Car('black', 'Acura', 'TSX')
        self.assertIsInstance(c, BaseVehicle)
