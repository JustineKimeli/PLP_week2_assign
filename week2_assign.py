# Week Two Assignment
my_list=[]
#Append 10,20,30,40 to my list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
# insert 15 to the second position in my list
my_list.insert(2,15)
#extend my_list with 50,60,70
list2=[50,60,70]
my_list+=list2

# Remove the last element from my list
my_list.pop(-1)

# sort my list in ascending orde
my_list.sort()

#find and print the index and value 30 in the list
index=my_list.index(30)
print(f"The index of the value 30 is at {index}")

print(my_list)


