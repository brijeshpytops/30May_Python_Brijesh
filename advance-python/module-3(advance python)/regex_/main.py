# import re

# # print(dir(re))

# data = "my birth date is 23-12-1996 and my brother birth date is 1/06/1994. 1_2_2004"

# pattern ={
#     'format-1': r'\b\d{1,2}-\d{1,2}-\d{4}\b',
#     'format-2': r'\b\d{1,2}/\d{1,2}/\d{4}\b',
#     'format-3': r'\b\d{1,2}_\d{1,2}_\d{4}\b'

# } 

# dates = []
# for key in pattern.keys():
#     dates.extend(re.findall(pattern[key], data))
# print(dates)


# import re

# def validate_mobile_number(number):
#     # Define regex pattern to allow spaces or dashes between digits
#     pattern = re.compile(r'^(\+?\d{1,3}[- ]?)?(\d{3}[- ]?\d{3}[- ]?\d{4})$')
    
#     # Match the pattern
#     if pattern.match(number):
#         return True
#     else:
#         return False

# # Test cases
# test_numbers = [
#     '1234567890',         # Valid
#     '+911234567890',      # Valid
#     '123-456-7890',       # Valid
#     '123 456 7890',       # Valid
#     '123456789',          # Invalid (only 9 digits)
#     '12345',              # Invalid (only 5 digits)
#     '+91 1234567890',     # Valid
#     '+91-1234567890',     # Valid
#     '12-34567890',        # Invalid (wrong format)
# ]

# for number in test_numbers:
#     print(f"{number}: {validate_mobile_number(number)}")


# import re

# def find_emails(text):
#     # Define regex pattern for email addresses
#     pattern = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')
    
#     # Find all matching patterns in the text
#     emails = pattern.findall(text)
    
#     return emails

# # Sample text for testing
# sample_text = """
#     Here are some emails: test.email+regex@gmail.com, first.last@example.co.uk, simple@example.com.
#     Invalid emails: test.email@.com, test@com, @example.com
# """

# # Find emails in the sample text
# emails = find_emails(sample_text)
# print(emails)


import re

# def replace_emails(text):
#     # Define regex pattern for email addresses
#     pattern = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')
    
#     # Replace all matching patterns in the text with [EMAIL]
#     replaced_text = pattern.sub('[EMAIL]', text)
    
#     return replaced_text

# # Sample text for testing
# sample_text = """
#     Here are some emails: test.email+regex@gmail.com, first.last@example.co.uk, simple@example.com.
#     Invalid emails: test.email@.com, test@com, @example.com
# """

# # Replace emails in the sample text
# replaced_text = replace_emails(sample_text)
# print(replaced_text)


# data =  "The kumbhmela conduct in guj"

# print(re.sub('guj', 'UP', data))


# import re

# def match_email(text):
#     # Define regex pattern for email addresses
#     pattern = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')
    
#     # Check if the text starts with an email address
#     match = pattern.match(text)
    
#     if match:
#         return match.group()
#     else:
#         return None

# # Test case
# text1 = "test.email+regex@gmail.com is a valid email."
# text2 = "This text starts with invalid.email@.com."

# print(match_email(text1))  # Output: test.email+regex@gmail.com
# print(match_email(text2))  # Output: None


# import re

# def search_email(text):
#     # Define regex pattern for email addresses
#     pattern = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')
    
#     # Search for an email address in the text
#     match = pattern.search(text)
    
#     if match:
#         return match.group()
#     else:
#         return None

# # Test cases
# text1 = "You can contact us at test.email+regex@gmail.com for more information."
# text2 = "No valid email here."

# print(search_email(text1))  # Output: test.email+regex@gmail.com
# print(search_email(text2))  # Output: None


# import re

# def validate_password(password):
#     # Define regex pattern for a strong password
#     pattern = re.compile(
#         r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
#     )
    
#     # Match the pattern
#     if pattern.match(password):
#         return True
#     else:
#         return False

# # Test cases
# passwords = [
#     'Password123!',    # Valid
#     'password123!',    # Invalid (no uppercase letter)
#     'PASSWORD123!',    # Invalid (no lowercase letter)
#     'Password!',       # Invalid (no digit)
#     'Password123',     # Invalid (no special character)
#     'Pass1!',          # Invalid (too short)
# ]

# for pwd in passwords:
#     print(f"{pwd}: {validate_password(pwd)}")
