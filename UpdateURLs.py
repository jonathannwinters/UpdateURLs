#!/usr/bin/python

__appname__ = "UpdateURLs"
__author__  = "Jonathan N. Winters"
__email__ = "jnw25@cornell.edu"
__version__ = "0.1"
__license__ = "GPL"
__description__ = "This Python script accepts three arguments, a given directory, text to search for, and the text replacement.  It will recusively go through every HTML,  HTM, PY and PHP, RB file in the given directory and subdirectory and replace the search text with the given replacement text. "

import sys, os
# set variables given as arguments
rootdir = sys.argv[1]
text_to_search_for = sys.argv[2]
text_replacement = sys.argv[3]
extensions = ["html", "htm", "py", "rb", "php"]

#recursively walk through each folder
for root, subfolders, files in os.walk(rootdir):
    for filename in files:
        extension = filename.split(".")[-1]
        #match file types to ["html", "htm", "py", "rb", "php"]
        if extension in extensions:
            with open(root + "/" + filename) as fh:
                #replace text_to_search_for with the text_replacement string
                text = fh.read().replace(text_to_search_for, text_replacement)
            with open(root + "/" + filename, "w") as fh:
                #rewrites updated text back to file
                fh.write(text)
