
import re

text = "Python is easy. Python is powerful. I love Python."
result1 = re.match("Python", text)
if result1:
    print("Match:", result1.group())
else:
    print("No match found")


result2 = re.search("easy", text)
if result2:
    print("Search:", result2.group())
else:
    print("No match found")

result3 = re.findall("Python", text)
print("Find All:", result3)
