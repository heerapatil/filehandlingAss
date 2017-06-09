def file(fname):
        with open (fname, "r") as f:
                data=f.readlines()
                print(data)
file('text.txt')
