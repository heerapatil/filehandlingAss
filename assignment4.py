# Question 4: Write a Python program to read last n lines of a file and display the same

def file(fname, nlines):  
        from itertools import islice  
        with open(fname) as f:  
                for line in islice(f, nlines):  
                        line.seek(0,2)
                        print(line)  
file("text.txt",2)  


'''
output:

'''
