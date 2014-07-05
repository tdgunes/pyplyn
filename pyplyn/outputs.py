# -*- coding: utf-8 -*-
"""
pyplyn.outputs
~~~~~~~~~~

Some useful output classes

Author: Taha Dogan Gunes
License: MIT, see LICENSE for more details.

"""

from . import elements

class Writer(elements.OutPypElement):
    """
    Writes the data to a text file
    """

    def __init__(self, path):
        self.output_file = open(path, 'w')

    def extract(self, data):
        self.output_file.write(data)

    def close(self):
        self.output_file.close()


class LineWriter(Writer):
    """
    Writes the data per line
    """

    def extract(self, data):
        super(LineWriter, self).extract(data + "\n")

class Printer(elements.OutPypElement):
    """
    Simple data printer
    """
    def close(self):
        pass

    def extract(self, data):
        print data


class Gatherer(elements.OutPypElement):
    """
    Outputs are gathered in to the pool inside this gatherer class
    after pipe is totally flowed, you can access the data by accesing to
    self.pool list
    """
    def __init__(self):
        self.pool = []

    def extract(self, data):
        self.pool.append(data)

    def close(self):
        pass
