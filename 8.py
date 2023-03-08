def count_upper_lower(string):
    # Initialize the counters for upper case and lower case letters
    upper_count = 0
    lower_count = 0
    
    # Loop through the characters in the string
    for char in string:
        # Check if the character is an upper case letter
        if char.isupper():
            upper_count += 1
        # Check if the character is a lower case letter
        elif char.islower():
            lower_count += 1
    
    # Print the results
    print("Number of upper case letters:", upper_count)
    print("Number of lower case letters:", lower_count)
# Call the function with the string "This Is A Test"
count_upper_lower("This Is A Test")
