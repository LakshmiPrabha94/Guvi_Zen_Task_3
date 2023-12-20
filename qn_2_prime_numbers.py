#Name: Lakshmi Prabha
#Program : Creates two lists - one for even numbers and another for odd numbers from the given list. 
#Version: 1
#Programming Language : Python
#Python Version: 3.12.0

# Given list
given_list = [10, 501, 22, 37, 100, 999, 87, 351]

# Initialize an empty list to store prime numbers
prime_numbers = []

# Iterate through each element in the given list
for num in given_list:
    # Check if the number is prime
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            # If not prime, break the inner loop
            break
    else:
        # If the loop completes without finding a divisor, the number is prime
        if num > 1:
            prime_numbers.append(num)

# Count the prime numbers
count = len(prime_numbers)

# Display the result
print("Given List:", given_list)
print()
print("Prime Numbers List:", prime_numbers)
print("Count of Prime Numbers:", count)
print()