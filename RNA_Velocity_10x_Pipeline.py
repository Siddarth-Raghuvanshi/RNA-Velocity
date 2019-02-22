from File_GUI import Get_Files
import os

#Import Files for the loom contruction from the GUI
Gene_File, Output_Folder = Get_Files()

print("Sorting the BAM file in /outs by cellbarcode")

#Run Samtools Sort initiall allow for the tool to run on a laptop by presorting the BAM file. Compression is set at 5 to improve both space savings and speed
os.system("samtools sort -l 5 -t CB -O BAM -o %s/outs/cellsorted_possorted_genome_bam.bam %s/outs/possorted_genome_bam.bam" %(Output_Folder,Output_Folder))
# NOTE Due to the possible issues associated with the large file created by the Samtools,
# NOTE it might be worth allowing people to adjust varible in the sort function in the future.

print("BAM File Sorted by Samtools")



print("Running RNA Velocity program on the Given 10x Folder and Gene Annotation File")

#Run Velocity Command
os.system("velocyto run10x %s %s" % ( Output_Folder,Gene_File))

print("Pipeline finished! The loom file should be inside the 10x folder in a Veloctyo Folder")
