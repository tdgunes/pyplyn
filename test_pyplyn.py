#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyplyn as p


c = p.Pipe()
c.add(p.LineReader("./test/input.txt"))
c.add(p.Lambda(lambda x:x+"asdasd"))
c.add(p.Writer("./test/output-new.txt"))
c.run()


#
# first_pipe = p.Pipe(name="first")
# first_pipe.add(p.LambdaFilter(lambda x:  "hello" in x))
# first_pipe.add(p.LambdaExtension(lambda x: x.title()))
#
#
# second_pipe = p.Pipe(name="second")
# second_pipe.add(p.LambdaFilter(lambda x: "world" in x))
# second_pipe.add(p.LambdaExtension(lambda x: x.upper()))
#
#
#
# main_pipe = p.Pipe(name="main")
# main_pipe.add(p.LineReader("./test/input.txt"))
# main_pipe.add(p.OutDuplicator(first_pipe, second_pipe))


# combine_pipe = p.Pipe(name="combine")
# combine_pipe.add(p.InDuplicator(p.LineReader("./test/output-1.txt"), p.LineReader("./test/output-2.txt")))
# combine_pipe.add(p.LambdaExtension(lambda x: " ".join([i.strip() for i in x])))
# combine_pipe.add(p.LambdaExtension(lambda x: x+"\n"))
# combine_pipe.add(p.Writer("./test/output-3.txt"))
# combine_pipe.run()


# combine_pipe = p.Pipe(name="combine")
# combine_pipe.add(p.InDuplicator(p.OutDuplicator(first_pipe, second_pipe)))
# combine_pipe.add(p.LambdaExtension(lambda x: " ".join([i.strip() for i in x])))
# combine_pipe.add(p.LambdaExtension(lambda x: x+"\n"))
# combine_pipe.add(p.Writer("./test/output-3.txt"))
# combine_pipe.run()

# pipes = [main_pipe, combine_pipe]
# for pipe in pipes:
#     pipe.run()




# class MongoCollection(p.InPypElement):
#     def __init__(self, db, collection):
#         self.collection = pymongo.MongoClient()[db][collection]
#     def grasp(self):
#         for document in self.collection:
#             yield document