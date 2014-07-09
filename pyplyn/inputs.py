# -*- coding: utf-8 -*-
"""
pyplyn.inputs
~~~~~~~~~~

Some useful output classes

Author: Taha Dogan Gunes
License: MIT, see LICENSE for more details.

"""
from . import elements


class LineReader(elements.PypElement):
    """
    Gives lines to our pipe
    """

    def __init__(self, path=""):
        super(LineReader, self).__init__(path=path)

    def output(self):
        with open(self.inputs["path"], "r") as input_file:
            for line in input_file:
                yield {"data": line}


class ListGiver(elements.PypElement):
    """
    Gives list elements to our pipe
    """

    def __init__(self, items=[]):
        super(ListGiver, self).__init__(items=items)

    def output(self):
        for item in self.inputs["items"]:
            yield {"data": item}

