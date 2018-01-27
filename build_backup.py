# usr/bin/env python3
import os
import sys
import random
import re
print('python select_structure_Energy_data.py PdbID template work_name appendix')

Dir_download = '/scratch/xc25/download'
PdbID = sys.argv[1]
Temp = sys.argv[2]
Work = sys.argv[3]
Appd = sys.argv[4]
if Work == 'ER':
   Work_whole = PdbID + '-' + Work
else:
   Work_whole = PdbID + '-' + Temp + '-'+ Work
SumD = Work_whole + '-' + Appd
os.system("mkdir Backup")
dir_backup = '/scratch/xc25/Backup'
os.chdir("%s"%(dir_backup))
os.system("mkdir %s"%(PdbID))
dir_PdbID = dir_backup + '/' + PdbID
os.chdir("%s"%(dir_PdbID))
os.system("mkdir %s"%(SumD))
dir_SumD = dir_PdbID + '/' + SumD
os.chdir("%s"%(dir_SumD)) 
os.system("mkdir Basefile")
dir_basefile = dir_SumD + '/Basefile'
dir_Target = '/scratch/xc25/' + PdbID + '/' + SumD + '/' + Work_whole + '0'
os.system("cp -R %s/* %s/"%(dir_Target,dir_basefile))  
for i in range(20):
    File = Work_whole + str(i)
    os.system("mkdir %s"%(File))
    dir_File = dir_SumD + '/' + File
    dir_Target = '/scratch/xc25/' + PdbID + '/' + SumD + '/' + File
    os.system("cp %s/energy*  %s/"%(dir_Target,dir_File))
    os.system("cp %s/dump*   %s/"%(dir_Target,dir_File))
    os.system("cp %s/wham*   %s/"%(dir_Target,dir_File))
    os.system("cp %s/*.in   %s/"%(dir_Target,dir_File))
    os.system("cp %s/*.slurm   %s/"%(dir_Target,dir_File))


 



