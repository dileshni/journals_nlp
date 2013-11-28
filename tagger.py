#!/usr/bin/python

import sys,os
from xml.etree.cElementTree import ElementTree, parse, Element, tostring
import nltk

path = "./tempsplit/"

dir = os.listdir(path)

#iterates through all of abstract's elements and child elements and gets text content
def get_abstract_text(absnode):
    L = []
    for elem in absnode.iter():
        text = elem.text
        if text and text.strip():
            L.append(text)
    return ' '.join(L)

for fname in dir:
    fh = open(path + fname)
    dom = parse(fh)
    elem = dom.getroot()
    abstract = elem.find(".//abstract")
    print("================== OK HERE WE GO ================== "+fname)
    try:
            sentences = nltk.sent_tokenize(get_abstract_text(abstract))
            sentences = [nltk.word_tokenize(sent) for sent in sentences]
            sentences = [nltk.pos_tag(sent) for sent in sentences]
            print sentences
    except:
            pass
    print("================== END  ==================")


