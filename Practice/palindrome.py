def check_palindrome(input_string):
    # 1. Normalize the string: convert to lowercase
    clean_string = input_string.lower()
    
    # 2. Reverse the string using slicing [start:stop:step]
    reversed_string = clean_string[::-1]
    
    # 3. Check for palindrome
    is_palindrome = (clean_string == reversed_string)
    
    return {
        "original": input_string,
        "reversed": reversed_string,
        "is_palindrome": is_palindrome
    }

# Example usage:
result = check_palindrome("car")
print(result)