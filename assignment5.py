#5. Write a Python program to read a file line by line and store it into a list. 

def read_file(fname):  
 with open(fname) as f:        
  print(f.readlines())  
 
read_file("text.txt")
 
'''output:
['hello people\n', 'hi\n', 'how\n', 'are\n', 'you\n']
'''
 
  
