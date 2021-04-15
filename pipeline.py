
#Python libs
from tkinter import filedialog
from tkinter import *

import subprocess as sp
import os,sys


#Own libraries
import practicals as pr



#Initiation

#My path
myp = os.path.dirname(os.path.abspath(__file__)) + os.sep




root = Tk()
root.withdraw()
folder_selected = filedialog.askdirectory()
print(folder_selected)

pr.setWD(folder_selected)


print("   ---   \n")

#Convert to Niix
pr.cnvrt(folder_selected)

print("   ---   \n")
#Moves files
pr.mvr(folder_selected)

print("   ---   \n")
#Create folder for results
pr.createresultfolder(folder_selected)

print("   ---   \n")



#Call SVRTK via Python via Shell
p = sp.call("./runDSVR.sh")
