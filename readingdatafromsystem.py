

# reading data from system
file_object = open("file.txt","r")

# storing the information contains in file.txt in st
st = file_object.read()
file_object.close()
# printing the information on command line

print (st)

