# Bruce Maxwell
# Spring 2015
# CS 151 project 6
#
# Program for converting a set of ps files to pngs using convert
# The ImageMagick convert function must be installed
#
# uses the -background white and -alpha remove commands to install
# a solid white background on the image
#

import os
import sys

if len(sys.argv) < 2:
    print "Usage: python %s <ps file 1> ..." % (sys.argv[0])
    exit(-1)

for f in sys.argv[1:]:
    words = f.split('.')
    cmd = "convert %s -background white -alpha remove %s.png" % (f, words[0])
    print cmd
    os.system(cmd)

