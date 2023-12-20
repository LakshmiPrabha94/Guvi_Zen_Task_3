#Name: Lakshmi Prabha
#Program : Identify a sublist in the list [4, 2, -3, 1, 6] whose sum equals to 0
#Version: 1
#Programming Language : Python
#Python Version: 3.12.0

given_list = [4, 2, -3, 1, 6]

# Flag to track whether a sublist is found
sublist_found = False

# Iterate through all possible sublists
for start in range(len(given_list)):
    sublist_sum = 0  # Initialize the sum for each sublist

    for end in range(start, len(given_list)):
        sublist_sum += given_list[end]  # Add the current element to the sublist sum

        # Check if the sublist sum equals 0
        if sublist_sum == 0:
            print("Sublist found:", given_list[start:end + 1])
            sublist_found = True
            break  # Optional: If you want to find only one sublist, you can break out of the inner loop here

    if sublist_found:
        break  # Break out of the outer loop if a sublist is found

# If no sublist is found
if not sublist_found:
    print("No sublist found.")
