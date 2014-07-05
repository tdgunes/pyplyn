#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyplyn as p

pipe = p.Pipe()
pipe.add(p.ListGiver([1, 2, 3, 4]))
pipe.add(p.Negation(p.LambdaFilter(lambda x: x > 1)))
pipe.add(p.Printer())
pipe.run()
