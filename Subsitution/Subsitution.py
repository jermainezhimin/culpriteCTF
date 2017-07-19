#!/usr/bin/env python
# Skeleton code to communicate with challenge server
import operator
from random import shuffle
import sys

def subCipher(infile, outfile, mode):

    #new string to write
    converted=""
    #Reading the infile
    with open(infile,'r') as f:
        data = f.read()
        f.close
        print "Input file completely read"


    #To encrypt we will have to go from decrypt to encrypt
    encList = ['2', 'b', 'm', 'j', 's', 'w', '0', 'n', 'f', 
               'r', '(', '4', 'a', '5', 'h', '}', 'v', ' ', 
               'i', 'u', '{', 'c', ')', 't', 'o', 'd', 'g', 
               'l', '.', ',', 'e', '3', 'y', 'p', 'k']

    #To decrypt we will have to go from encrypt to decrypt
    decList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 
               'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 
               't', 'u', 'v', 'w', 'y', '0', '2', '3', '4', 
               '5', ' ', ',', '.', '(', ')', '{', '}']   

    # Checking uniqueness of characters
    # lis = []
    # for a in data:
    #     if not (a in lis):
    #         lis.append(a)
    # print lis
    # print len(lis)

    # shuffle(decList)
    # print decList
    print "Encrypting/Decrpyting Text"
    
    for b in range(0,len(data)):
        
        if (mode=="encrypt"):
            converted += encList[decList.index(data[b])]

        elif (mode=="decrypt"):
            converted += decList[encList.index(data[b])]

    with open(outfile,'w') as f:
        f.write(converted)
        f.close
        
    print "Output file completely written"

subCipher("Cipher.txt","CipherEnc.txt","encrypt")
subCipher("CipherEnc.txt","CipherDec.txt","decrypt")

# if __name__ == '__main__':
#   infile = sys.argv[1]
#   outfile = sys.argv[2]
#   mode = sys.argv[3]
#   subCipher(infile, outfile, mode)
