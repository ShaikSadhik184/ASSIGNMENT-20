import string

def is_pangram(string):
    # Convert the string to lower case
    string = string.lower()
    
    # Remove any punctuation from the string
    string = string.translate(str.maketrans("", "", string.punctuation))
    
    # Create a set of the letters in the string
    letters = set(string)
    
    # Check if the set of letters is equal to the set of all lower case letters in the alphabet
    return set(string.ascii_lowercase) <= letters
# Call the function with the pangram "The quick brown fox jumps over the lazy dog"
print(is_pangram("The quick brown fox jumps over the lazy dog"))
