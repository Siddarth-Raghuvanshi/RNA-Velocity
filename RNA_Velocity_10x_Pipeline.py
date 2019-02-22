#!/usr/bin/env python3

import numpy as np
from File_GUI import Get_Files
import os

#Import Files for the loom contruction from the GUI
Output_Folder, Gene_File = Get_Files()

#Run Samtools Sort initiall allow for the tool to run on a laptop by presorting the BAM file. 
os.system("samtools sort -l 0 -O BAM  %s/outs/possorted_genome_bam.bam -o %s/outs/cellsorted_possorted_genome_bam.bam" %(Output_Folder,Output_Folder))
# NOTE Due to the possible issues associated with the large file created by the Samtools,
# NOTE it might be worth allowing people to adjust varible in the sort function in the future.

#Run Velocity Command
os.system("velocyto run10x %s %s" % (Output_Folder, Gene_File,))
