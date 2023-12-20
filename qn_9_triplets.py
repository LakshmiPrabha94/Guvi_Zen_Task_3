#Name: Lakshmi Prabha
#Program : Identify a triplet in the list [10, 20, 30, 9] whose sum equals the given value of 9
#Version: 1
#Programming Language : Python
#Python Version: 3.12.0

given_list = [10, 20, 30, 9]
given_value = 59
triplet_found = False  # Flag to track whether a triplet is found

# Find a triplet whose sum is equal to the given value
for i in range(len(given_list) - 2):
    for j in range(i + 1, len(given_list) - 1):
        for k in range(j + 1, len(given_list)):
            if given_list[i] + given_list[j] + given_list[k] == given_value:
                print("Triplet found:", given_list[i], given_list[j], given_list[k])
                triplet_found = True  # Set the flag to True when a triplet is found
                break  # Optional: If you want to find only one triplet, you can break out of the loop here

    if triplet_found:
        break  # Break out of the outer loop if a triplet is found

# If no triplet is found
if not triplet_found:
    print("No triplet found.")
