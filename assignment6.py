#6. Write a Python program to read a file line by line store it into a variable. 

def file(fname):
        with open (fname, "r") as f:
                data=f.readlines()
                print(data)
file('text.txt')


'''output:
['hello people\n', 'hi\n', 'how\n', 'are\n', 'you\n']
'''

