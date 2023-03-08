def is_palindrome(s):
    # Convert the string to lowercase and remove all non-alphanumeric characters
    s = ''.join(e for e in s if e.isalnum()).lower()
    
    # Reverse the string
    s_rev = s[::-1]
    
    # Compare the original and reversed strings
    if s == s_rev:
        return True
    else:
        return False
# Check if the string "racecar" is a palindrome
is_palindrome_racecar = is_palindrome("racecar")
print(is_palindrome_racecar)  # Output: True

# Check if the string "hello" is a palindrome
is_palindrome_hello = is_palindrome("hello")
print(is_palindrome_hello)  # Output: False
