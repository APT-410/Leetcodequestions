import re
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def is_palindrome(s):
    logging.debug(f"Original string: {s}")
    
    # Remove spaces and convert to lower case
    s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    logging.debug(f"Processed string (alphanumeric, lowercase): {s}")
    
    # Check if the string is equal to its reverse
    if s == s[::-1]:
        logging.debug(f"The string '{s}' is a palindrome.")
        return True
    else:
        logging.debug(f"The string '{s}' is NOT a palindrome.")
        return False

# Testing the function
test_strings = ["Racecar", "Hello", "A man a plan a canal Panama", "Python", "Madam, I'm Adam"]
for text in test_strings:
    logging.info(f'Testing string: "{text}"')
    result = is_palindrome(text)
    logging.info(f'Result: "{text}" is a palindrome: {result}')


#I used this as as a simple debugging challenge 
#original question to debug is the following code
'''
def is_palindrome(s):
    # Remove spaces and convert to lower case
    s = s.replace(" ", "").lower()
    # Check if the string is equal to its reverse
    if s == s[::-1]:
        return True
    else:
        return False

# Testing the function
test_strings = ["Racecar", "Hello", "A man a plan a canal Panama", "Python"]
for text in test_strings:
    print(f'"{text}" is a palindrome:', is_palindrome(text))
'''