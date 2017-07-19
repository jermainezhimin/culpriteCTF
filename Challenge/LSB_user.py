#!/usr/bin/env python
import argparse

from PIL import Image
import binascii
import copy

#main file that runs the parsing and extraction of PNG
def extractMain(infile, outfile, interval):

    #print string updates and modes
    print "Infile: " + str(infile) +  " and Outfile: " + str(outfile)
    print 'Extract message with "'+ str(interval) + '" interval'
    
    #reading the png
    pixList = parsePNG(infile)

    #processing hidden msg via LSB extraction
    hidMsg = extractLSB(pixList, interval)

    with open(outfile,'w') as f:
        f.write(hidMsg)
        f.close()
    
    return

#parsing the PNG file
def parsePNG(infile):
    
    pixList =[]
    
    #reading the image and pixels
    #return a list of binary RGB bytes values
    
    print "Parsed pixels from picture"
    
    return pixList

#extraction of the important bits
def extractLSB(pixList, interval):
    
    extList = copy.deepcopy(pixList)
    hidMsg = ""
    
    #reading the last bit of each byte
    #keep only the bits after each defined interval and convert to string equivalent
    
    print "Extracted message from picture"
    
    return hidMsg

#Functions to call to embed the text into image
#extractMain("XXX.png", "XXXExtract.mystery",X)
