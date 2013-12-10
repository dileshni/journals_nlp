#!/usr/bin/python

import sys,os
from xml.etree.cElementTree import ElementTree, parse, Element, tostring
import nltk
from nltk import FreqDist

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

    try:
        #get abstract text, normalize and encode with utf-8 to avoid issues with unicode
        abs_text = get_abstract_text(abstract)
        abs_text = (abs_text.encode('utf-8')).lower()
        word_tokens = nltk.word_tokenize(abs_text)

        #possibility of only finding frequency of nouns or pronous?? This will ignore words like those/might that provide no context
        #find the frequency of the words in the abstract
        fdis = FreqDist(word_tokens)
        #get keys of the frequent words
        vocab = fdis.keys()
        #use only frequent words that are longer than 4 chars and occurs at least twice(?)
        freq_words = sorted([w for w in vocab if len(w) > 4 and fdis[w] > 1])
        print freq_words

        print "-----------------END-------------"

    except:
        print "Unexpected error:", sys.exc_info()