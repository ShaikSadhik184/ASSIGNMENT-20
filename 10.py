def is_anagram(str1, str2):
    # Convert the strings to lower case and remove any spaces
    str1 = str1.lower().replace(" ", "")
    str2 = str2.lower().replace(" ", "")
    
    # Check if the lengths of the strings are equal
    if len(str1) != len(str2):
        return False
    
    # Create dictionaries of the letter frequencies in each string
    dict1 = {}
    dict2 = {}
    for letter in str1:
        dict1[letter] = dict1.get(letter, 0) + 1
    for letter in str2:
        dict2[letter] = dict2.get(letter, 0) + 1
    
    # Check if the dictionaries are equal
    return dict1 == dict2
# Call the function with the strings "listen" and "silent"
print(is_anagram("listen", "silent"))
