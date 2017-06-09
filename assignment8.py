f=open("test.txt","r")
long=''
for l in f:
  if len(l)>len(long):
     long=l
 print long
