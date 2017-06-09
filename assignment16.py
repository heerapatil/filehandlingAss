#16. Write a Python program to remove newline characters from a file.
f=open("text.txt","r").readlines()
for s in f:
    s.rstrip("\n")
    print text.txt
