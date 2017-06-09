#7. Write a Python program to read a file line by line store it into an array. 

def file(fname):
        array = []
        with open(fname) as f:
                for line in f:
                     array.append(line)
                print(array[2])

file("text.txt")

'''output:
how
'''
