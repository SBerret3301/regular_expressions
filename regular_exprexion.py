import re

# Function to search for a word in a string
def search(string, word):
    # Compile a regex pattern to match the whole word
    pattern = re.compile(fr'\b{re.escape(word)}\b')
    return bool(pattern.search(string))

# Function to check if a string contains a digit
def num(string):
    return bool(re.search(r'\d', string))

# Function to replace spaces with hyphens in a string
def replace(string):
    return re.sub(r'\s', '-', string)

# Function to validate a phone number in the format XX-XXX-XXXX
def phone(number):
    return bool(re.search(r'\d{2}-\d{3}-\d{4}', number))

# Function to validate an email address
def email(email):
    return bool(re.search(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email))

# Test cases
string = "one piece 3amek ."
word = "no"
print(search(string, word))

digit_test = "websites devloper"
print(num(digit_test))

space_test = "hello everyone"
print(replace(space_test))

email_test = "salaheddineberret@gmail.com"
print(email(email_test))

number_test = "87-788-9870"
print(phone(number_test))