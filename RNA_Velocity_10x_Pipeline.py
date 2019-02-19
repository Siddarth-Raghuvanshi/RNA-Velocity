Command#!/usr/bin/env python3

import numpy as np
from File_GUI import Get_Files
import os

#Import Files for the loom contruction from the GUI
Output_Folder, Gene_File = Get_Files()

#Run Velocity Command
os.system("velocyto run10x %s %s" % (Gene_File, Output_Folder))
