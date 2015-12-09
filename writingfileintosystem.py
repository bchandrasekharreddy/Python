# writing the file into our system

file_object = (open("file.txt","w"))

# creating new variable consists of string

st = input("enter string")

file_object.write(st)

file_object.close()

