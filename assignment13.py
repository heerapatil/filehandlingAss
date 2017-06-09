from shutil import copyfile 
import os
os.system("touch file1.txt")
copyfile("text.txt","file1.txt")
print file1
