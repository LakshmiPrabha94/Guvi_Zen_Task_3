#Name: Lakshmi Prabha
#Program : distribute a given list of N integers, representing the number of mangoes in each bag, among M students in a Guvi class such that each student receives exactly one bag? 
#The objective is to minimize the difference between the number of mangoes in the bag with the maximum and minimum mangoes given to the students.
#Version: 1
#Programming Language : Python
#Python Version: 3.12.0

# Given list of mangoes
mangoes_in_bag = [5, 10, 3]
number_of_students = 2

# Step 1: Sort the list of mangoes
sorted_mangoes = sorted(mangoes_in_bag)

# Step 2: Calculate the number of mangoes each student will get
bags_per_student = len(sorted_mangoes) // number_of_students
remaining_bags = len(sorted_mangoes) % number_of_students

# Step 3: Initialize variables to track the distribution
distribution = []
start_index = 0

# Step 4: Distribute mangoes among students
for i in range(number_of_students):
    # Determine the range of bags for the current student
    end_index = start_index + bags_per_student + (1 if i < remaining_bags else 0)
    
    # Get the bags for the current student
    student_bags = sorted_mangoes[start_index:end_index]
    distribution.append(student_bags)

    # Update the starting index for the next student
    start_index = end_index

# Print the distribution
print("Distribution of mangoes:", distribution)
