# -*- coding: utf-8 -*-
"""
pyplyn.elements
~~~~~~~~~~

This module implements the Pyplyn Fundamental Elements

Author: Taha Dogan Gunes
License: MIT, see LICENSE for more details.

"""
import abc


class PypElement(object):
    __metaclass__ = abc.ABCMeta


class MidPypElement(PypElement):
    __metaclass__ = abc.ABCMeta


class InPypElement(PypElement):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def grasp(self):
        """
        Every input pipe need to implement this must have a yield
        in it
        :return:
        """


class OutPypElement(PypElement):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def extract(self, data):
        """
        Every output pipe need to implement this, like outputting
        to file or db

        :param data:
        :return:
        """

    @abc.abstractmethod
    def close(self):
        """
        Close the pyp, like a_file.close() or stop db connection

        :return:
        """


class FilterPypElement(MidPypElement):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def stay(self, data):
        """
        Every filter pipe needs to implement this
        return true to have the data
        return false to decline it

        :param data:
        :return:
        """


class ExtendPypElement(MidPypElement):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def extend(self, data):
        """
        Every filter pipe needs to implement this
        return true or false

        :param data:
        :return:
        """
