def file(fname):
        array = []
        with open(fname) as f:
                for line in f:
                     array.append(line)
                print(array)

file("text.txt")

'''output:
['hello people\n', 'hi\n', 'how\n', 'are\n', 'you\n']
'''
