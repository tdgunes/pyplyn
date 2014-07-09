# -*- coding: utf-8 -*-
"""
pyplyn.outputs
~~~~~~~~~~

Some useful output classes

Author: Taha Dogan Gunes
License: MIT, see LICENSE for more details.

"""

from . import elements


class Writer(elements.PypElement):
    """
    Writes the data to a text file
    """

    def __init__(self, path):
        super(Writer, self).__init__(path=path)
        self.f = open(self.inputs["path"], "w")
    def output(self):
        self.f.write(self.inputs["data"])


class LineWriter(elements.PypElement):
    """
    Writes the data per line
    """

    def __init__(self, path):
        super(LineWriter, self).__init__(path=path)

    def output(self):
        with open(self.inputs["path"], "w") as f:
            f.write(self.inputs["data"] + "\n")
            yield None


class Printer(elements.PypElement):
    """
    Simple data printer
    """

    def __init__(self):
        super(Printer, self).__init__()

    def output(self):
        print self.inputs["data"]
        yield self.inputs["data"]


class Gatherer(elements.PypElement):
    """
    Outputs are gathered in to the pool inside this gatherer class
    after pipe is totally flowed, you can access the data by accesing to
    self.pool list
    """

    def __init__(self):
        super(Gatherer, self).__init__()
        self.pool = []

    def output(self):
        self.pool.append(self.inputs["data"])
        yield self.pool


