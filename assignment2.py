f=open("file.txt","w+")
f.write("hello")
f.write("how are you")
f.write("hi")
f.write("gfhagfa")
f.write("cfjzgc")
f.seek(3,0)
print(f.readLine())
f.close()