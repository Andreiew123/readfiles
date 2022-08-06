# -*- coding: utf8 -*-
from __future__ import unicode_literals
import codecs
def reading(file,typ):
    with codecs.open(file, "r", 'utf-8') as f:
            if typ == "r":
                return f.read()
            elif typ == "rl":
                return f.readline()
            elif typ == "rls":
                return f.readlines()

def writting(file,opt,txt):
    temp = ""
    with codecs.open(file,opt,'utf-8') as f:
        if type(txt) == list:
            for _ in txt:
                temp = temp + str(_)
            txt = temp
        return f.write(txt)
