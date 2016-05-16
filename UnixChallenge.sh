#!/bin/shALL

grep 'gene      '  /home/bryan/data/TEST_Homo_sapiens.GRCh38.78.gtf | cut -f1,3-5,9-17 >  Hs_gene.txt

grep 'CDS       ' /home/bryan/data/TEST_Homo_sapiens.GRCh38.78.gtf | cut -f1,3-5,9-17 > Hs_CDS.txt

grep 'transcript        ' /home/bryan/data/TEST_Homo_sapiens.GRCh38.78.gtf | cut -f1,3-5,9-17 > Hs_transcript.txt
