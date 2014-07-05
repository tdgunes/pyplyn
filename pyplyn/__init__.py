# -*- coding: utf-8 -*-

"""
pyplyn, only one-way pipeline
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
__title__ = 'pyplyn'
__version__ = '0.1.5'
__author__ = 'Taha Dogan Gunes'
__license__ = 'MIT'
__copyright__ = 'Copyright 2014 Taha Dogan Gunes'

# Set default logging handler to avoid "No handler found" warnings.

from .elements import ExtendPypElement, MidPypElement, OutPypElement, InPypElement, FilterPypElement, PypElement
from .inputs import LineReader, ListGiver
from .middles import LambdaExtension, LambdaFilter, Negation, UniqueFilter
from .outputs import LineWriter, Writer, Printer
from .pyp import Pipe


import logging

try:  # Python 2.7+
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass

logging.getLogger(__name__).addHandler(NullHandler())
