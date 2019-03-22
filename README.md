# RNA Velocity

# About
This is a pipeline to easily run the RNA velocity program (http://velocyto.org/). Currently, the GUI is used to run the 10x version of velocyto. 

## Setup
To run the script, ensure you have Anaconda,Samtools and Velocity installed

## How to use
Ensure that you have the folder that contains the output file from the cellranger pipeline as well as a gene annotation file. Here is a link to a MM-10 Gene Annotation file from my dropbox. 

```
https://www.dropbox.com/s/mtr5jde54vn76rk/mm10-genes.gtf?dl=0
```

To run the program. 

Navigate to the folder in terminal/Cmd and type in

```
python RNA_Velocity_10x_Pipeline.py
```

Follow the prompts on screen. 


# Notes
The GUI program also currently does not accept any additional commands. This will be added in the future. 
