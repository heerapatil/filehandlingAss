#1. Write a Python program to read an entire text file and print its contents.
f=open("file1.txt","w+")
f.write("hello people, how are you all")
f.seek(0,0)
print(f.read())
f.close()
'''output:
hello people, how are you all
'''
