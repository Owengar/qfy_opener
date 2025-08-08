import sys
sys.dont_write_bytecode = True

import sys, os
import psutil
import subprocess
import shutil
import time



parent_pid = int(sys.argv[1])
source_path = sys.argv[2]



output = open(source_path + "\\mover_says_hi.txt", "w")
sys.stdout = output 
sys.stderr = output


while psutil.pid_exists(parent_pid):
    pass
print(parent_pid)
print(source_path)
print(psutil.pid_exists(parent_pid))

try:
    os.remove(source_path + "\\open_quantify.exe")
except:
    pass


while True:
    try:
        time.sleep(1)
        print("tried again")
        shutil.copyfile(source_path + "\\new_opener.exe", source_path + "\\open_quantify.exe")
        break
    except:
        pass

subprocess.run(source_path + "\\open_quantify.exe", shell=True)
