
import re

text = "My phone number is 9876543210"
result = re.search("phone", text)

if result:
    print("Word found:", result.group())
else:
    print("Word not found")

digits = re.findall(r"\d", text)
print("Digits:", digits)
number = re.search(r"\d{10}", text)

if number:
    print("Phone Number:", number.group())
else:
    print("Phone number not found")
result = re.match("My", text)

if result:
    print("String starts with:", result.group())
else:
    print("Pattern not matched")
