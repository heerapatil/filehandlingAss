#12. Write a Python program to copy the contents of a file to another file . 

from shutil import copyfile 
import os
os.system("touch test.txt")
copyfile("text.txt","test.txt")
'''output:
hello people
hi
how
are
you
fsdfgsdhf
dfsfksdf
dfsdfsdf
