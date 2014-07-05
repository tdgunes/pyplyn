# -*- coding: utf-8 -*-
"""
pyplyn.middles
~~~~~~~~~~

Some useful middle classes

Author: Taha Dogan Gunes
License: MIT, see LICENSE for more details.

"""
from . import elements


class LambdaExtension(elements.ExtendPypElement):
    """
    Gets a function and applies the function to data that
    it receives
    """

    def __init__(self, func):
        self.func = func

    def extend(self, data):
        return self.func(data)


class LambdaFilter(elements.FilterPypElement):
    """
    Gets a function and decides whether data can stay or not
    based on that function
    """

    def __init__(self, func):
        self.func = func

    def stay(self, data):
        return self.func(data)


class UniqueFilter(elements.FilterPypElement):
    """
    Saves the data arrived, and stops the same data if
    received
    """

    def __init__(self):
        self.arrived = set()

    def stay(self, data):
        if not data in self.arrived:
            self.arrived.add(data)
            return True
        return False


class Negation(elements.FilterPypElement):
    """
    Reverses the effect of any filter
    NegationFilter(NegationFilter(UniqueFilter())) is same as
    just UniqueFilter()
    """

    def __init__(self, filter_element):
        self.filter_element = filter_element

    def stay(self, data):
        return not self.filter_element.stay(data)

