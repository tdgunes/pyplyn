pyplyn: One-way only pipeline for data handling
===============================================

.. image:: https://badge.fury.io/py/pyplyn.svg
    :target: http://badge.fury.io/py/pyplyn


.. image:: https://img.shields.io/pypi/dm/pyplyn.svg
    :target: https://crate.io/packages/pyplyn/

.. image:: https://img.shields.io/pypi/l/pyplyn.svg
    :target: https://github.com/tdgunes/pyplyn/blob/master/LICENSE

Pyplyn is an MIT Licensed simple flow-based data handling structure for making
data handling repetitive tasks, easily without repeating yourself for every
different scenario.

It is based on Python's lovely generators, so for every data flow into the pipe
is in an iterative fashion. It is currently used in a research project to handle
some repetitive daily tasks. (Moving, filtering, altering the data)

Still the pyplyn module that is used in the project has some dirty but useful
components like progressbar, ML based classification filter and so on, with this
simple library, I think there can be a common simple ground for handling our
repetitive tasks.

Installation
============

In order to install pyplyn, just simply:

.. code-block:: bash

    pip install pyplyn

Or alternatively, download the package from pypi_, extract and execute:

.. code-block:: bash

    python setup.py install

.. _pypi: http://pypi.python.org/pypi/pyplyn

Quick Start
===========

Pyplyn aims to make data handling in a flow based fashion:

.. code-block:: python

    import pyplyn as p

    pipe = p.Pipe()
    pipe.add(p.LineReader("hello.txt"))
    pipe.add(p.LambdaFilter(lambda line: len(line) < 50))
    pipe.add(p.LineWriter("small_hello.txt"))
    pipe.run()

You can even write your own Pyp modules as simple as this:

.. code-block:: python

    import pyplyn as p
    import pymongo

    class MongoCollection(p.InPypElement):
        def __init__(self, db, collection):
            self.collection = pymongo.MongoClient()[db][collection]
        def grasp(self):
            for document in self.collection:
                yield document

Add this new pipe element to your current flow by:

.. code-block:: python

    pipe = p.Pipe()
    pipe.add(MongoCollection("data","raw"))
    pipe.add(p.LambdaExtension(lambda document: document["text"])
    pipe.add(p.LineWriter("data_text.txt"))

Has a simple API:

.. image:: http://tdgunes.org/pyplyn.png
   :width: 900px
   :height: 198px

Why is it so called 'one-way'?
==============================
Simplicity is the ultimate aim, however there is a experimental branch multi-pyplyn in the project currently, I am just
experimenting to find an elegant and easy to use API for the library.

Documentation
=============
Sorry, it is currently not available, but I recommend you to check the source, it is
pretty straightforward for now.

Contribute
==========
Any contribution is welcome.
