#Name: Lakshmi Prabha
#Program : Find the first non-repeating element in given list of numbers
#Version: 1
#Programming Language : Python
#Python Version: 3.12.0


#numbers = [1, 1, 2, 3, 4, 4, 5, 6, 7, 5]
numbers = list(input("Enter a list of numbers"))
non_repeating_element = None

# Iterate through the list
for number in numbers:
    # Check if the count of the current number is 1 (non-repeating)
    if numbers.count(number) == 1:
        non_repeating_element = number
        break  # Break out of the loop once the first non-repeating element is found

# Print the result
if non_repeating_element is not None:
    print("The first non-repeating element is:", non_repeating_element)
else:
    print("No non-repeating element found.")
