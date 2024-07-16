# Task 1
text = input('Enter your text: ')
count_b = text.count('b')
print(f"Number of 'b' in the entered text: {count_b}")
# Task 2
def is_valid_name(name):
    if name. isalpha() and name[0]. isupper() and name[1:1].islower():
        return True
    return False
name = input("Enter you`re name: ")
if is_valid_name(name):
    print(f"Name '{name}' is valid")
else:
    print(f"Name '{name}' is not valid")
# Task 3
text = input('Enter a string: ')
sum_of_codes = sum(ord(char) for char in text)
print(f"The sum of all character codes in the entered string is: {sum_of_codes}")
# Task 4
pi = 3.1415926535
for i in range(2, 12):
    print(f"{pi:.{i}f}")
# Task 5
text = input("Enter your text: ")
words = text.split()
longest_word = max(words, key=len)
print(f"The longest word is: '{longest_word}'")
# Task 6
text = input("Enter your text: ")
words = text.split()
small_word = min(words, key=len)
print(f"The small word is: '{small_word}")
# Task 7
import re
def remove_html_tags(text):
    clean_text = re.sub(r'<.*?>', '', text)
    return clean_text
html_text = input("Введіть текст з HTML-тегами: ")
cleaned_text = remove_html_tags(html_text)
print("Cleaned text:", cleaned_text)