def square_list():
    # Create an empty list to store the squares
    squares = []
    
    # Loop through the numbers 1 to 30
    for num in range(1, 31):
        # Calculate the square of the number and append it to the list
        squares.append(num ** 2)
    
    # Return the list of squares
    return squares
# Print the list of squares from 1 to 30
squares = square_list()
print(squares)
