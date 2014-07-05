#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyplyn as p

pipe = p.Pipe()
pipe.add(p.LineReader("hello.txt"))

pipe.add(p.ListGiver([1, 2, 3, 4]))
pipe.add(p.Negation(p.LambdaFilter(lambda x: x > 1)))
pipe.add(p.LineWriter())
pipe.run()

class MongoCollection(p.InPypElement):
    def __init__(self, db, collection):
        self.collection = pymongo.MongoClient()[db][collection]
    def grasp(self):
        for document in self.collection:
            yield document