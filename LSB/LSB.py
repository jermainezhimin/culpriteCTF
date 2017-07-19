#!/usr/bin/env python
import argparse

from PIL import Image
import binascii
import copy

def extractMain(infile, outfile, interval):

    #print string updates and modes
    print "Infile: " + str(infile) +  " and Outfile: " + str(outfile)
    print 'Extract message with "'+ str(interval) + '" interval'

    pixList = parsePNG(infile)
    hidMsg = extractLSB(pixList, interval)

    with open(outfile,'w') as f:
        f.write(hidMsg)
        f.close()
    
    return

def embedMain(infile, outfile, message, interval):

    #takes in large messages as input
    with open(message,'r') as f:
        message = f.read()
        f.close

    #message binary
    binMsg = ''.join(format(ord(a), '08b') for a in message)

    #print string updates and modes
    print "Infile: " + str(infile) +  " and Outfile: " + str(outfile)
    print 'Embedding message "'+ str(message) + '" '
    #print the file in binary does not work for huge text files
    #print 'Embedding message "'+ str(message) + '": ' + binMsg
    print 'Embedding interval with "'+ str(interval) + '" interval'

    pixList = parsePNG(infile)
    modPixList = embedLSB(pixList,binMsg,interval)
    processingPNG(infile,outfile, modPixList)
    
    return

def processingPNG(infile, outfile, newPixList):
    oriIm = Image.open(infile)
    modIm = oriIm.copy()
    pixel = modIm.load()
    indPix = []
    pixArray = []
    
    #converting all binary to integers
    for a in range(0,len(newPixList)):
        newPixList[a]=int(newPixList[a],2)

    #converting to processing format
    for b in range(0,len(newPixList)/3):
        for c in range(0,3):
            #writing the pixel RGB 
            indPix.append(newPixList [b*3+c])
        #append the pixels to a array
        pixArray.append(tuple(indPix))
        indPix = []

    print "Processed binary input into RGB"

    #writing the pixel files into the image
    for a in range(modIm.size[0]):
        for b in range(modIm.size[1]):
            pixel[a,b] = pixArray[a*modIm.size[1]+b]

    print "Completed writing pixels for modified image"

    #saving image
    modIm.save(outfile)
    return


def parsePNG(infile):
    
    #reading the image and pixels
    Im = Image.open(infile)
    pixel = Im.load()
    pixList = []

    #return image formats and size is in x and then y
    print "Image format: " + str(Im.format) + " and Image size: " + str(Im.size) + " and Image mode: " + str(Im.mode)
    print str(Im.size[0] * Im.size[1] * 3) + " writable bits equivalent to " + str((Im.size[0] * Im.size[1])/8.0) + " writable bytes"

    for a in range(Im.size[0]):
        for b in range(Im.size[1]):
            for c in range(0,len(pixel[a,b])):
                
                #converts the pixel into binary
                pixList.append(bin(pixel[a,b][c]))

    #stripping all 0b from the strings
    for d in range(0,len(pixList)):
            pixList[d]=pixList[d].replace('0b','')

    return pixList

def embedLSB(pixList, hiddenMsg, interval):

    counter=0
    countList = []
    modPixList = copy.deepcopy(pixList)

    print "Writing " + str(len(hiddenMsg)) + " bits"
                           
    #creating the index sequence to embed
    for a in range(0,len(hiddenMsg)):
        
        if len(hiddenMsg) <= 1:
            print "There is no message input"
            break

        else:
            if (a==0):
                countList.append(a)
            else:
                countList.append(a*(interval+1))

    #inserting the bits
    for b in countList:
        modPixList[b] = modPixList[b][0:(len(modPixList[b])-1)] + hiddenMsg[counter]
        counter += 1

    #Prints the list pattern and does not work for large text files
    #print "List pattern of " + str(countList)
    
    return modPixList

def extractLSB(pixList, interval):
    
    extList = copy.deepcopy(pixList)
    counter = 0
    lastBit =""
    hidBit =""
    hidMsg = ""
    
    
    #extracting last bits for all of the picture
    for a in range(0, len(extList)):
        lastBit += extList[a][(len(extList[a])-1):]

    print "Extracted last bits of the picture file"
    
    #dropping of the interval bits
    for b in range(0, len(lastBit)):
        if (b == 0):
            hidBit += lastBit[b]

        elif (counter == interval):
            hidBit += lastBit[b]
            counter = 0

        elif (counter != interval):
            counter += 1

    #dropping off any incomplete bits
    if (len(hidBit)%8 != 0):
        print "Dropping off " + str(len(hidBit)%8) + "bits" 
        hidBit = hidBit[:-(len(hidBit)%8)]

    #formatting the string into a list of 8 charas
    hidList = map(''.join, zip(*[iter(hidBit)]*8))

    #conversion from binary back to string
    for c in range(0,len(hidList)):
        hidList[c] = chr(int(hidList[c], 2))
        hidMsg += hidList[c]

    print "Extracted message from picture"
    
    return hidMsg

#Functions to call to embed the text into image
#embedMain("Image.jpg","ImageEmbed.png","Embed.txt",4)
#embedMain("Image.jpg","ImageEmbed.png","Embed.txt.zip",4)

#Functions to call to embed the text into image
#extractMain("ImageEmbed.png", "Extract.mystery",4)
extractMain("ImageEmbed.png", "Extract.mystery",4)
'''
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Extractor of hidden message from picture')
    parser.add_argument('-i', dest='infile',help='input file')
    parser.add_argument('-o', dest='outfile',help='output file')
    parser.add_argument('-m', dest='message',help='message')
    args = parser.parse_args()

    infile, outfile, message = args.infile, args.outfile, args.message
    main(infile, outfile,message)
'''
