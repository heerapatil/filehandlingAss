#11. Write a Python program to write a list to a file.
import simplejson
f = open("test.txt", "w")
simplejson.dump([1,2,3,4], f)
f.close()
