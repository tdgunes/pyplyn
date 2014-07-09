# -*- coding: utf-8 -*-
"""
pyplyn.pyp
~~~~~~~~~~

This module implements the Pyplyn Pyp aka Pipe

Author: Taha Dogan Gunes
License: MIT, see LICENSE for more details.

"""
from . import elements


class Pipe(object):
    """
    The class handles pipe elements, runs them.
    """

    def __init__(self, name=""):
        self.elements = []
        self.in_pipe = None
        self.other_pipes = None
        self.out_pipe = None
        self.name = name


    def add(self, element):
        """
        Adds a pipe element to pipe
        :param element:
        :return:
        """
        self.elements.append(element)


    def assert_tail(self):
        """
        This assertion will be called just in SwitchPypElement's Tail Pipes

        :param other_pipes:
        :param output_pipe:
        :return:
        """
        assert isinstance(self.out_pipe, elements.OutPypElement), 'Wrong output element type, want a OutPypElement!'
        for other_pipe in self.other_pipes:
            assert isinstance(other_pipe, elements.MidPypElement), 'Wrong middle element type, want a MidPypElement!'


    def assert_head(self):
        assert isinstance(self.in_pipe, elements.InPypElement), 'Wrong input element type, want a InPypElement!'

    def define_tail(self):
        self.other_pipes = self.elements[1:-1]
        self.out_pipe = self.elements[-1]
        self.assert_tail()

    def define_head(self):
        self.in_pipe = self.elements[0]
        self.assert_head()

    def divide(self):
        assert len(self.elements) >= 2, "In order flow, pipe needs 2 or more elements"
        self.define_head()
        self.define_tail()

    def iterate(self, data):
        write = True
        for element in self.other_pipes:
            if isinstance(element, elements.ExtendPypElement):
                data = element.extend(data)
            elif isinstance(element, elements.FilterPypElement):
                if not element.stay(data):
                    write = False
                    break

        if write:
            self.out_pipe.extract(data)

    def run(self):
        """
        Let the pipe flow
        :return:
        """

        self.define_head()
        self.define_tail()

        for data in self.in_pipe.grasp():
            self.iterate(data)
