#10. Write a Python program to get the file size of a plain file. 
import os
st=os.stat("text.txt")
print st.st_size

'''output:
70
'''
