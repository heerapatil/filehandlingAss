'''#16. Write a Python program to remove newline characters from a file.
f=open("text.txt","r").readlines()
for s in f:
    s.rstrip("\n")
    print text.txt
'''
def remove_newlines(fname):
    flist = open(fname).readlines()
    return [s.rstrip('\n') for s in flist]

print(remove_newlines("test.txt"))
