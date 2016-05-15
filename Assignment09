#!/usr/bin/python
import sys
import os

#creating filenames
infname    = sys.argv[1]
fastaname  = infname + ".fasta"
mafftfname = fastaname + ".mafft"
stockname  = mafftfname + ".stock"

#simple to fasta
handle = open(infname, "r")
outf   = open(fastaname, "w")
for line in handle:
	linearr = line.split()
	seqid   = linearr[0]
	seq     = linearr[1]
	outf.write(">%s\n%s\n" % (seqid, seq))
handle.close()
outf.close()	

#align using mafft

cmd = "mafft %s > %s" % (fastaname, mafftfname)
sys.stderr.write("command: %s\n" % cmd)
os.system(cmd)
sys.stderr.write("command done")

#convert fasta maft alignment to stockholm
cmd = "fasta_to_stockholm %s > %s" % (mafftfname,stockname)
sys.stderr.write("command: %s\n" % cmd)
os.system(cmd)
sys.stderr.write("command done\n")

#run quicktree to get distance matrix
cmd = "quicktree -out m %s" % stockname
#sys.stderr.write("command: %s\n" % cmd)
os.system(cmd)
#sys.stderr.write("command done \n")
