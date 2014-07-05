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

    def __init__(self):
        self.elements = []

    def add(self, element):
        """
        Adds a pipe element to pipe
        :param element:
        :return:
        """
        self.elements.append(element)

    @staticmethod
    def make_assertions(input_pipe, other_pipes, output_pipe):
        """
        To assure that the pipe is correctly settled
        :param input_pipe:
        :param other_pipes: can be []
        :param output_pipe:
        :return:
        """
        assert isinstance(input_pipe, elements.InPypElement), 'Wrong input element type, want a InPypElement!'
        assert isinstance(output_pipe, elements.OutPypElement), 'Wrong output element type, want a OutPypElement!'
        for other_pipe in other_pipes:
            assert isinstance(other_pipe, elements.MidPypElement), 'Wrong middle element type, want a MidPypElement!'


    def run(self):
        """
        Let the pipe flow
        :return:
        """
        assert len(self.elements) >= 2, "In order flow, pipe needs 2 or more elements"
        in_pipe = self.elements[0]
        other_pipes = self.elements[1:-1]
        out_pipe = self.elements[-1]

        self.make_assertions(in_pipe, other_pipes, out_pipe)

        for data in in_pipe.grasp():
            write = True

            for element in other_pipes:
                if isinstance(element, elements.ExtendPypElement):
                    data = element.extend(data)
                elif isinstance(element, elements.FilterPypElement):
                    if not element.stay(data):
                        write = False
                        break
            if write:
                out_pipe.extract(data)
