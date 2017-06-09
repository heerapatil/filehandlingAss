#10. Write a Python program to get the file size of a plain file. 
import os
'''def getSize(file):
    st = os.stat(file)
    return st.st_size
print getSize("text.txt")
'''
st=os.st_size("text.txt")
print st

'''output:
70
'''
