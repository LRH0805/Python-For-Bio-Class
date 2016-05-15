#!/usr/bin/python
import sys

fname        = sys.argv[1] #contains barcoded sequences
barcodefname = sys.argv[2] #contains list of barcodes

barcodefile = open(barcodefname, "r") #defining barcodefile
for barcode in barcodefile:
        barcode = barcode.strip() #making barcode an item
        outfname = "%s.%s" % (fname,barcode) #naming output file for each barcode
        print "barcode: %s" % barcode #print each barcode to screen
        outf = open(outfname, "w") #open the file we are writing to
        handle = open(fname, "r") #read the file with the barcode sequences
        for line in handle: #for each seqeunce in the fname
                temp = line.split() #split the line (seq# and sequence)
                potential_barcode = temp[1][:len(barcode)] #potential barcode is the second item and is the from the length of the barcode to the beginning
                if potential_barcode == barcode:
                        outseq = temp[1][len(barcode):] #outseq is the rest of the matched sequence without the barcode
                        print(temp[0] + " " + outseq) #print the seq# and the outseq
                     outf.write(temp[0] + " " + outseq + "\n") #write to the file
        handle.close()
        outf.close()
barcodefile.close()
