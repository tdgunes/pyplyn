# -*- coding: utf-8 -*-
"""
pyplyn.middles
~~~~~~~~~~

Some useful middle classes

Author: Taha Dogan Gunes
License: MIT, see LICENSE for more details.

"""
from . import elements


class Lambda(elements.PypElement):
    """
    Gets a function and applies the function to data that
    it receives
    """

    def __init__(self, func):
        super(Lambda, self).__init__(func=func)


    def output(self):
        func = self.inputs["func"]
        yield {"data": func(self.inputs["data"])}


class UniqueFilter(elements.PypElement):
    """
    Saves the data arrived, and stops the same data if
    received
    """
    def __init__(self):
        super(UniqueFilter, self).__init__()
        self.arrived = set()

    def output(self):
        self.arrived.add(self.inputs["data"])
        if not self.inputs["data"] in self.arrived:
            self.arrived.add(self.inputs["data"])
            yield {"data":self.inputs["data"]}