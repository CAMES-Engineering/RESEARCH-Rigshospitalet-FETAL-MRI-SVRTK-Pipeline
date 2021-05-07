# RESEARCH Rigshospitalet FETAL MRI SVRTK Pipeline
 Automation of the pipeline in using SVRTK libraries on FETAL MRI data. For scientific research purposes only.


 ## Purpose
 The sole purpose of this library is to make running of SVRTK (link) libraries easier for medical researchers.




 ## Prerequisites
 Installed [ SVRTK ](https://github.com/SVRTK/SVRTK "GitHub")  
 Installed [ dcm2niix ](https://github.com/rordenlab/dcm2niix "GitHub")

 ## Installation
 Download the repositoty

 Open terminal at repository (Right click and choose, open terminal at folder)

  write command *chmod u+x run.sh*  
  write command *chmod u+x runDSVR.sh*


  ## Run
  Open terminal at repository (Folder with code that you've downloaded) (Do so by right click and choose: open terminal at folder). Now run the command

  ./run.sh

  Choose patient folder (Stacks in STACKS and Mask in MASK)
  Choose Template stack

  Wait for SVRTK to run

  Resulting file is in the "out" folder
