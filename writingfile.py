# creating object where it stores file name as well as mode w means write
file_object = open("chandu.txt","w")

pharse = raw_input("enter string to store in the file")


file_object.write(pharse)
file_object.close()


file_objcet1 = open("chandu.txt","r")



print "contnet in file is"+ file_objcet1.read()
