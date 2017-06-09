#11. Write a Python program to write a list to a file.
'''import simplejson
f = open("test.txt", "w")
simplejson.dump([1,2,3,4], f)
f.close()
'''

list=["one","two","three"]
with open("text.txt", "w") as f:
        for l in list:
                f.write("%s\n" % l)

content = open("text.txt")
print(content.read())
