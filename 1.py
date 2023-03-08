def get_unique_list(lst):
    # Create an empty list to hold the unique elements
    unique_list = []
    
    # Loop through each element in the original list
    for elem in lst:
        # If the element is not already in the unique list, add it
        if elem not in unique_list:
            unique_list.append(elem)
    
    # Return the unique list
    return unique_list
# Define a list with duplicate elements
my_list = [1, 2, 3, 2, 4, 3, 5]

# Get a new list with only the unique elements
unique_list = get_unique_list(my_list)

# Print the unique list
print(unique_list)  # Output: [1, 2, 3, 4, 5]
