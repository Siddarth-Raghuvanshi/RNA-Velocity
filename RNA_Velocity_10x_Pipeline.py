Command#!/usr/bin/env python3

import numpy as np
from File_GUI import Get_Files
import os

#Import Files for the loom contruction from the GUI
Gene_File, Output_Folder = Get_Files()

#Run Velocity Command
os.system("velocyto run10x %s %s" % ( Output_Folder,Gene_File))
