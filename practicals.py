import os
import subprocess as sp

myp = os.path.dirname(os.path.abspath(__file__)) + os.sep


def cnvrt(pathin):
    if not os.path.exists(pathin+os.sep + "converted"): #Avoid conversion if already there. Applicable at rerun
        # Loop all and convert
        for root, dirs, files in os.walk(pathin + os.sep + "STACKS" + os.sep, topdown=False):
            for d in dirs:
                print(d)
                p = sp.call(["dcm2niix", root+d])
    else:
        print("Rerun: Conversion Skipped")


def mvr(pathin):

    pathin_c = pathin+os.sep + "converted" + os.sep

    if not os.path.exists(pathin_c):
        os.mkdir(pathin_c)


    for root, dirs, files in os.walk(pathin, topdown=False):
        for f in files:
            if f.endswith(".nii"):
                print(root,f)
                os.rename(root+os.sep+f,pathin_c+f)


    for root, dirs, files in os.walk(pathin_c, topdown=False):
        for f in files:
            if f.endswith(".nii"):
                os.rename(root+os.sep+f,root+os.sep+f.split("_")[-1])


def createresultfolder(pathin):

    if not os.path.exists(pathin +os.sep + "out"):
        os.mkdir(pathin + os.sep + "out")



def getWD():
    with open( "WD.CAMES", 'r') as f:
        WD = f.readlines()[0]
    return WD


def setWD(folder_selected):
    with open(myp + os.sep + "WD.CAMES", 'w') as f:
        f.write(folder_selected + os.sep)


def listdatainput(dirdir):
    print("Python - Practicals: Listing data input")
    mylist = []
    for root, dirs, files in os.walk(dirdir, topdown=False):
        for f in files:
            print(f)
            mylist.append(f)

    print("\n List: ", mylist )
    return mylist



def getmaskpath(dirdir):
    print("Python - Practicals: Obtaining Mask")
    for root, dirs, files in os.walk(dirdir, topdown=False):
        for f in files:
            if not f.endswith("_Store"):
                if not f.endswith(".here"):
                    print(f)
                    return f
