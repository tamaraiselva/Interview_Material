import re

# Sample input string
input_string = "Alice is 24 years old, and her brother Adam is 17."

# Task 1: Find all words that start with the letter 'a' (case insensitive)
words_starting_with_a = re.findall(r'\b[aA]\w*\b', input_string)

print("Words starting with 'a':", words_starting_with_a)

# Task 2: Replace all digits with '#'
replaced_string = re.sub(r'\d', '#', input_string)

print("String after replacing digits:", replaced_string)

# output

# Words starting with 'a': ['Alice', 'and', 'Adam']
# String after replacing digits: Alice is ## years old, and her brother Adam is ##.