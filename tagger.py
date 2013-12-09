#!/usr/bin/python

import sys,os
from xml.etree.cElementTree import ElementTree, parse, Element, tostring
import nltk

path = "./tempsplit/"

dir = os.listdir(path)
interesting_tags = ['CD','FW','JJ','NN','NNP','NNPS','NNS','VB','VBD','VBG','VBN','VBP','VBZ']
delchars = ''.join(c for c in map(chr, range(256)) if not c.isalnum())

#iterates through all of abstract's elements and child elements and gets text content
def get_abstract_text(absnode):
    L = []
    for elem in absnode.getiterator():
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
            sentences = nltk.sent_tokenize(get_abstract_text(abstract).encode('utf-8'))
            sentences = [nltk.word_tokenize(sent) for sent in sentences]
            sentences = [nltk.pos_tag(sent) for sent in sentences]
            for sentence in sentences:
                for word in sentence:
                    term = word[0]
                    # Sanitation
                    term = term.strip(delchars)
                    tag = word[1]
                    #print tag,":",term
                    if len(term) > 0:
                        if tag in interesting_tags:
                            if tag == "CD" and len(term) < 4:
                                pass
                            else:
                                print tag,":",term
                        else:
                            #print "I'm ignoring:" + term
                            pass
            #print sentences
    except:
            pass
    print("================== END  ==================")


