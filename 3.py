def print_even_numbers(lst):
    # Loop through each element in the list
    for num in lst:
        # Check if the element is even
        if num % 2 == 0:
            # If the element is even, print it
            print(num)
# Print the even numbers in the sample list
print_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9])
