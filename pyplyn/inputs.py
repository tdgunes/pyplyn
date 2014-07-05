# -*- coding: utf-8 -*-
"""
pyplyn.inputs
~~~~~~~~~~

Some useful output classes

Author: Taha Dogan Gunes
License: MIT, see LICENSE for more details.

"""
from . import elements


class LineReader(elements.InPypElement):
    """
    Gives lines to our pipe
    """

    def __init__(self, path):
        self.path = path

    def grasp(self):
        with open(self.path, "r") as input_file:
            for line in input_file:
                yield line


class ListGiver(elements.InPypElement):
    """
    Gives list elements to our pipe
    """

    def __init__(self, items):
        self.items = items

    def grasp(self):
        for item in self.items:
            yield item
