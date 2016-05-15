# Python-For-Bio-Class
This repo contains the files from my spring 2016 Python Programming for Biology class at the University of Florida. 

#Assignment06 = Python Adding Program
Takes an input file of numbers sepreated by spaces or tabs, adds them, and then prints the sum.

#Assignment07 = Sequence Barcode Identifier
Takes 2 command line arguments: a DNA barcode and a file containing DNA sequences. This program prints the DNA sequences from the file that match the given DNA barcode, throwing away the barcode.

#Assignment08 = Barcode Parser
Takes 2 command line arguments: a file with barcoded DNA sequences and a file with barcodes. The outputs are a file for each barcode. The output files are called "inputfilename.barcode" for each barcode from the input barcode file. Each file contains the sequences that matched that barcode, without the barcode identifier.

#Assignment09 = Mini Bioinformatics Pipeline using Mafft and Quicktree
Takes 1 command line argument: the name of a file with unaligned DNA sequences in a simple sequence file format. This program prints the pairwise distances among all the pairs of sequneces to the screen. It aligns the sequences using mafft, converts the mafft alignment from fasta to stockholm format, then uses quicktree to calculate the distance matrix.

#Assignment10 = Mean and Standard Error Calculator from a Distance Matrix
Takes 1 command line argument: the name of a file of a distance matrix in quicktree format. This script calculates the mean and standard error of the upper diagonal of the distance matrix. It prints <mean> +/- <standard_error> as floating point numbers.
