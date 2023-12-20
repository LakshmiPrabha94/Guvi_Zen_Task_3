#Name: Lakshmi Prabha
#Program : Creates two lists - one for even numbers and another for odd numbers from the given list. 
#Version: 1
#Programming Language : Python
#Python Version: 3.12.0



# Given list
given_list = [10, 501, 22, 37, 100, 999, 87, 351]

# Initialize a variable to count happy numbers
happy_numbers_count = 0

# Iterate through each element in the given list
for original_num in given_list:
    # Set to store seen sums and avoid infinite loops
    seen_sums = set()
    num = original_num  # Use a temporary variable to avoid modifying the original value

    # Iterate until the sum becomes 1 (happy number) or repeats (not a happy number)
    while num != 1 and num not in seen_sums:
        seen_sums.add(num)
        num_sum = 0  # Temporary variable to store the sum of squares of digits

        # Calculate the sum of squares of digits
        for digit in str(num):
            num_sum += int(digit) ** 2

        num = num_sum  # Update 'num' with the calculated sum for the next iteration

    # If the sum is 1, the number is a happy number
    if num == 1:
        # If happy, increment the count
        happy_numbers_count += 1

# Display the result
print("Given List:", given_list)
print("Count of Happy Numbers:", happy_numbers_count)
