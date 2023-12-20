#Name: Lakshmi Prabha
#Program : Calculate the sum of the first and last elements. 
#Version: 1
#Programming Language : Python
#Python Version: 3.12.0


# Given integer
print()
number = input("Enter a number")

# Convert the integer to a list of its digits using split()
digit_list = list(map(int, str(number)))

# Display the result
print()
print("Integer to List:", digit_list)
print()


# Calculate the sum of the first and last elements
c = len(digit_list)
if c >= 2:  # Ensure there are at least two elements in the list
    my_sum = digit_list[0] + digit_list[c - 1]
    print("Sum of First and Last Elements:", my_sum)
else:
    print("Not enough elements to calculate the sum.")
