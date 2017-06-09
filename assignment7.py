def file(fname):
        array = []
        with open(fname) as f:
                for line in f:
                     array.append(line)
                print(array)

file("text.txt")
