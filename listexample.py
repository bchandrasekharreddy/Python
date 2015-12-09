mylist = []
# creating empty list

mylist.append(1)
# appending vaue to mylist

mylist.append(2)
mylist.append(3)
mylist.append(4)

#print mylist[0]
#printing the value of 0 index
#print mylist[1]
#print mylist[2]
#print mylist[3]
#print mylist[0]

# we can del element in list by giving the index number of it

del mylist[3]

len(mylist)

# by useing for loop we can print at a time

# by defining function we can add values in list
def sumvalues(A):
    result = 0
    for x in A:
        result = result +x
        return result

print sumvalues(mylist)


#print mylist
#print mylist[0]

# by runing for loop also we can add elements in the list

sum = 0
for i in mylist:
    if i<=len(mylist):
        sum = sum+i
        print sum   

#print sum(mylist)


    
    
    
