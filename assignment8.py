#8. Write a python program to find the longest words. 
f=open("text.txt","r")
long=" "
for l in f:
  if len(l)>len(long):
     long=l
  print long
