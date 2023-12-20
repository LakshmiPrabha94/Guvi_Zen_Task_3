#Name: Lakshmi Prabha
#Program : identify and display the duplicates among three given lists? use your own lists for demonstration.
#Version: 1
#Programming Language : Python
#Python Version: 3.12.0

# Creating three sample lists
list1 = [1, 2, 3, 4, 5, 2, 7, 8]
list2 = [5, 6, 7, 8, 9, 10, 5]
list3 = [8, 9, 10, 11, 12, 8, 14, 5]

# Converting lists to sets and finding the intersection (duplicates)
set1 = set(list1)
set2 = set(list2)
set3 = set(list3)

duplicates = set1 & set2 & set3

# Displaying the duplicates
print("Duplicates: ", list(duplicates))

