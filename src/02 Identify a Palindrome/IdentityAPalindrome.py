import re

def is_palindrome(text):
  tempStr = ""
  for char in text:
    if char.isalpha():
      tempStr = tempStr + char.lower()
  return tempStr.lower() == tempStr[-1::-1].lower()

result = is_palindrome("Go hang a salami, I’m a lasagna hog.")
print(result)
