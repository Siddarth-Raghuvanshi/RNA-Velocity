from tkinter import *
import numpy as np
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory
import os
from Bio.Alphabet import generic_dna
from Bio import SeqIO
from Bio.Seq import Seq


class GUI(object):

    def __init__(self, Master):
        self.row = 0
        self.Files = [[]]
        self.Files.append([])
        self.num_of_Additional = 0
        self.Win = Master

    #Button Functions
    def End(self):
        self.Win.quit()

    def File(self,FileName, Type, Count):
        if (Count == 0):
            File = askopenfilename()
        else:
            File = askdirectory()
        FileName["text"] = os.path.basename(File)
        self.Files[0].append(File)
        if(Type == "R"):
            self.Files[1].append(Count)
        else:
            self.Files[1].append(Type)

    def Add(self):
        self.Done.grid(row = self.row + 3, column = 0, pady = 50)
        self.A_Seq.grid(row = self.row + 2, column = 0, pady = 0,)
        self.Organizer("Additional command", "R")
        self.row += 3

    def Get_Rid(self,Frame, Prompt, index):
        Frame.destroy()
        Prompt.destroy()
        self.Filetypes[index + 2] = 0

    #Function to create headings and buttons
    def Organizer(self, Heading, Type):

        #Create a Prompt and a Frame
        Prompt = Label(self.Win, text = Heading)
        F = Frame(self.Win)

        #Display the prompt
        Prompt.grid(row = self.row, column = 0,pady = 5, padx = 100)
        self.row += 1

        #IF this is an add button, follow this code to display it
        if (Type == "ADD"):
            More = Button(F,text = "Add More", command = self.Add)
            More.grid(row = self.row, column = 0)
            self.row += 1

        #IF this isn't an add button, run this code to display the buttons
        else:
            Count = self.num_of_Additional
            if(Count < 2):
                FileName = Button(F,text = "File Name", command = lambda: self.File(FileName,Type, Count))
                FileName.grid(row = 0, column = 2)
                self.num_of_Additional += 1
            if(Count > 1):
                Command = Entry(F)
                Command.grid(row = 0, column = 2)


            if(Type == "R"):
                Remove = Button(F,text = "Remove", command = lambda: self.Get_Rid(F,Prompt, Count))
                Remove.grid(row = 0, column = 6)
                F.grid(row = self.row, column = 0)
                self.row += 1
                self.num_of_Additional += 1


        return F

    def run(self):

        self.Win.title("RNA Velocity ")

        self.T_Seq = self.Organizer("Please select the Gene Annotation File", "Gene_Anno")
        self.T_Seq.grid(row = self.row, column = 0)
        self.row += 1

        self.G_Seq = self.Organizer("Please select a file inside the 10x Output Folder", "Output_File")
        self.G_Seq.grid(row = self.row, column = 0)
        self.row += 1

        self.A_Seq= self.Organizer("Do you wish to add any additional commands", "ADD")
        self.A_Seq.grid(row = self.row, column = 0)
        self.row += 1

        #Done Button
        self.Done = Button(self.Win, text = "Done", command = self.End)
        self.Done.grid(row = self.row, column = 0, pady = 50)
        self.row += 1


def Get_Files():

    Root = Tk()
    Program = GUI(Root)
    Program.run()
    Root.mainloop()

    Gene_File = Program.Files[0][0]
    Output_Folder = Program.Files[0][1]

    #Add code submiting for additional commands

    Root.destroy()

    return( Gene_File, Output_Folder)
