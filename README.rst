pyplyn: One-way only pipeline for data handling
===============================================

.. image:: https://badge.fury.io/py/pyplyn.svg
    :target: http://badge.fury.io/py/pyplyn


.. image:: https://pypip.in/d/pyplyn/badge.png
    :target: https://crate.io/packages/pyplyn/

.. image:: https://pypip.in/license/pyplyn/badge.png
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

In order to install pyplyn, just simply::

    pip install pyplyn

Or alternatively, download the package from pypi_, extract and execute::

    python setup.py install

.. _pypi: http://pypi.python.org/pypi/pyplyn

Quick Start
===========

Pyplyn aims to make data handling in a flow based fashion::

    import pyplyn as p

    pipe = p.Pipe()
    pipe.add(p.LineReader("hello.txt"))
    pipe.add(p.LambdaFilter(lambda line: len(line) < 50))
    pipe.add(p.LineWriter("small_hello.txt"))
    pipe.run()

You can even write your own Pyp modules as simple as this::

    import pyplyn as p
    import pymongo

    class MongoCollection(p.InPypElement):
        def __init__(self, db, collection):
            self.collection = pymongo.MongoClient()[db][collection]
        def grasp(self):
            for document in self.collection:
                yield document

Add this new pipe element to your current flow by::

    pipe = p.Pipe()
    pipe.add(MongoCollection("data","raw"))
    pipe.add(p.LambdaExtension(lambda document: document["text"])
    pipe.add(p.LineWriter("data_text.txt"))

..

Documentation
=============
Sorry, it is currently not available, but I recommend you to check the source, it is
pretty straightforward for now.

Contribute
==========
Any contribution is welcome.