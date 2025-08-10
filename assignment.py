# Creating an empty list named my_list
my_list = []

# Appending elements to my_list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)  


# Inserting values
my_list.insert(1, 15) # Insert 15 at second position

# extending the list with another list
my_list.extend([50, 60, 70]) 

# removing last element
my_list.pop()  

# sorting the list in ascending order
my_list.sort()

# find and print the index of value 30
index_of_30 = my_list.index(30)

print(f"The index of 30 is: {index_of_30}")