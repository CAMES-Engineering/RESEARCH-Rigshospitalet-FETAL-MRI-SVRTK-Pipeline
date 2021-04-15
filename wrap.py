
#Python libs
from tkinter import filedialog
from tkinter import *
import os,sys
import subprocess as sp

import practicals as pr

print("Python Wrap.py: Imports")


#My path
myp = os.path.dirname(os.path.abspath(__file__)) + os.sep
print("Python Wrap.py: Initiation")


WD = pr.getWD()
print("Python Wrap.py: WD Obtained: ", WD)




def callcreator(MYTYPE,INPUTFOLDER,OUTPUTFOLDER,STACK,MASK,TEMPLATE):
    stacks = STACK

    #Build call
    if MYTYPE == "SVR":
        funccall = "reconstruct"
    elif MYTYPE == "DSVR_B":
        funccall = "reconstructBody"


    call = [funccall,OUTPUTFOLDER +os.sep+ MYTYPE  +".nii", str(len(stacks))]

    for ss in stacks:
        call.append(INPUTFOLDER+os.sep+str(ss))



    call.append("-mask")
    call.append(MASK)


    call.append("-template")
    call.append(TEMPLATE)

    call.append("-default")

    # call.append("-remote")


    return call


print("DSVR")
inputfolder = WD+os.sep+"converted"
outputfolder = WD+os.sep+"out"

inputlist = pr.listdatainput(inputfolder)
# print(len(inputlist), "\n\n\n",inputlist)

maskname = pr.getmaskpath(WD+ os.sep + "MASK")
mask = WD+ os.sep + "MASK" + os.sep + maskname
# print(mask,inputlist)


root = Tk()
root.withdraw()
template = filedialog.askopenfilename(initialdir = inputfolder,title = "Select Template Stack")
print("Python - Wrap.py: Template selected: ", template)


print("Python Wrap: Creating Call \n\n\n\n\n")

call = callcreator("DSVR_B",inputfolder,outputfolder,inputlist,mask,template)
print("Call: \n", call)
with open(outputfolder + os.sep + "call.file",'w') as f:
    f.write(str(call))

print("Starting SVRTK \n\n\n\n\n")

p = sp.call(call)
