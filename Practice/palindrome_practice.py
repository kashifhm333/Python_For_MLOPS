def check(input_string):
    clean = input_string.lower()
    reversed_string = clean[::-1]
    is_it = (clean == reversed_string)
    
    return {
        "original": input_string,
        "reversed": reversed_string,
        "is_palindrome": is_it
    }

result = check("racecar")
print(result)