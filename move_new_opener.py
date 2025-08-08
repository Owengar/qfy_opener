import sys
sys.dont_write_bytecode = True

import sys, os
import psutil
import subprocess
import shutil



parent_pid = int(sys.argv[1])
source_path = sys.argv[2]

while psutil.pid_exists(parent_pid):
    pass

with open(source_path + "mover_says_hi.txt", "w"):
    pass

shutil.copyfile(source_path + "\\new_opener.exe", source_path + "\\open_quantify.exe")
subprocess.run(source_path + "\\open_quantify.exe", shell=True)