# RNA Velocity

# About
This is a pipeline to easily run the RNA velocity program (http://velocyto.org/). Currently, the GUI is used to run the 10x version of velocyto. 

## Setup
To run the script, ensure you have Anaconda and Velocity installed

## How to use
Ensure that you have the folder that contains the output file from the cellranger pipeline as well as a gene annotation file. Currently the program contains a a Gene Annotation file of the mm10-mouse annotation file from the cellranger file. To run the program. 

Navigate to the folder in terminal/Cmd and type in

```
python RNA_Velocity_10x_Pipeline.py
```

Follow the prompts on screen. 


# Notes
The GUI program also currently does not accept any additional commands. This will be added in the future. 
