# -*- coding: utf-8 -*-
"""
pyplyn.elements
~~~~~~~~~~

This module implements the Pyplyn Fundamental Elements

Author: Taha Dogan Gunes
License: MIT, see LICENSE for more details.

"""
import abc


class Pipe(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, elements=[]):
        self.elements = elements

    def add(self, element):
        self.elements.append(element)

    def run(self):
        for output in self.elements[0].output():
            print output
            self.elements[1].inputs = dict(self.elements[1].inputs.items() + output.items())
            for prev, item, nex in self.neighborhood(self.elements[1:]):
                gen = item.output()
                if nex:
                    next_element = next(gen)
                    nex.inputs = dict(nex.inputs.items() + next_element.items())

    @staticmethod
    def neighborhood(iterable):
        iterator = iter(iterable)
        prev = None
        item = iterator.next()  # throws StopIteration if empty.
        for nex in iterator:
            yield (prev, item, nex)
            prev = item
            item = nex
        yield (prev, item, None)


class PypElement(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, **kwargs):
        self.inputs = kwargs
        #print self.inputs

    @abc.abstractmethod
    def output(self):
        """
        Yield here
        :return:
        """



