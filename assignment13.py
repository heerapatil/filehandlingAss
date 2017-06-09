#13. Write a Python program to combine each line from first file with the corresponding line in second file. 

with open("text.txt") as f1, open("test.txt") as f2:
    for l1, l2 in zip(f1, f2):
       print(l1+l2)
