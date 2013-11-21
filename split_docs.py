import os,sys
from xml.etree.cElementTree import iterparse, tostring, parse, ElementTree

#for file in os.listdir('data'):
context = iter(iterparse("data/10000.xml",events=("start","end")))

#get root
event, root = next(context)
assert event == "start"

#split file by each journal using 'front' tag, and save to filesystem
for event, elem in context:
    if event == "end" and elem.tag == "journal":
        id = elem.find(".//id")
        try:
            tree = ElementTree(elem)
            tree.write("splitdata/"+ id.text)
            print id.text
            root.clear()
        except:
            print "unexpected error: ", sys.exc_info()[0]
            raise
