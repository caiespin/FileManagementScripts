import os
import pathlib
import glob
from shutil import copyfile

currentDir =  os.getcwd()

Lab = 'Lab4.asm'
TargetDir = '/'+Lab[:4]+'/MossSubmission'+Lab[:4]

if not os.path.exists(currentDir+TargetDir):
    os.mkdir(currentDir+TargetDir)

files = glob.glob('**/*.asm', recursive = True)

for file in files:
    if Lab in file or Lab.lower() in file:
        originDir = pathlib.PurePath(file)
        if Lab[:4] in str(originDir.parents[3]):
            StudentID = originDir.parts[-3]
            dest = currentDir+TargetDir+'/'+StudentID+'.asm'
            print(dest)
            copyfile(file, dest)
