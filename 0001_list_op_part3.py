# clear(): Removes all elements from the list.
list_num_1 = [1,2,3,4]
print("list_num_1: ",list_num_1)
list_num_1.clear()
print("list_num_1: ",list_num_1)

# index(): Returns the index of the first occurrence of a specified element.
list_num_2 = [1,2,3,4,1,3,4]
print("index of 3: ",list_num_2.index(3))

# count(): Returns the number of occurrences of a specified element.
list_num_3 = [1,2,3,4,1,3,4,1,2,1,4]
print("Count: ",list_num_3.count(4))

# sort(): Sorts the elements of a list.
list_num_4 = [1,2,3,4,1,3,4,1,2,1,4]
print(list_num_4)
list_num_4.sort(reverse=True)
print(list_num_4)

# reverse(): Reverses the order of the elements in the list.
list_num_5 = [1,2,3,4,5]
print(list_num_5)
list_num_5.reverse()
print(list_num_5)

# copy(): Returns a shallow copy of the list.
list_num_6 = [1,2,3,4]
new_list = list_num_6
print("List num: ",list_num_6)
print("New List: ",new_list)
new_list.append(99)
print("List num: ",list_num_6)
print("New List: ",new_list)
backup_list = list_num_6.copy()
print("Backup List: ",backup_list)
print("List num: ",list_num_6)
list_num_6.append(333)
print("Backup List: ",backup_list)
print("List num: ",list_num_6)


