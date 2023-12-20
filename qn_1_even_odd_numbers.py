#Name: Lakshmi Prabha
#Program : Creates two lists - one for even numbers and another for odd numbers from the given list. 
#Version: 1
#Programming Language : Python
#Python Version: 3.12.0

# Given list
given_list = [10, 501, 22, 37, 100, 999, 87, 351]

# Initialize empty lists to store even and odd numbers
even_numbers = []
odd_numbers = []

# Iterate through each element in the given list
for num in given_list:
    # Check if the number is even
    if num % 2 == 0:
        # If even, add it to the even_numbers list
        even_numbers.append(num)
    else:
        # If odd, add it to the odd_numbers list
        odd_numbers.append(num)

# Display the result
print()
print("Given List:", given_list)
print()
print("Even Numbers:", even_numbers)
print("Odd Numbers:", odd_numbers)
print()
