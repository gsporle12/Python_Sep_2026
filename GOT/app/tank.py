#! /usr/bin/env python3
# Author: Gsporle
# Version: 1.0
# Description: This script defines a class of Tank
"""
    Tank class for online game
"""

class Tank:
    # Class has TWO components: Attributes + Behaviour (Methods)
    def __init__(self, country, model):
        self.country = country
        self.model = model
        self._speed = 0
        self._direction = 0
        self._location = {"x": 0, "y": 0, "z": 0}
        self._shells = 20
        self._health = 100
        # No EXPLICIT return as method is IMPLICITLY called.

    def accel(self, increase):
        self._speed += increase
        return None

    def decel(self, decrease):
        self._speed -= decrease
        return None

    def rotate_left(self, degrees):
        self._direction -= degrees % 360
        return None

    def rotate_right(self, degrees):
        self._direction += degrees % 360
        return None

    def shoot(self):
        self._shells -= 1
        return None

    def take_damage(self, damage):
        self._health -= damage
        return None

    # Some SPECIAL Methods
    # Example of OPERATOR overloading
    def __add__(self, other):
        return self._health + other._health

    def __del__(self):
        print(f"Boom..Boom..Boom")
        return None

    # Example of a getter and a setter
    def get_health(self):
        return self._health

    def set_health(self, new_health):
        self._health = new_health
        return None