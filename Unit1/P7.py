student = {
    "name": "Harsh",
    "age": 21,
    "marks": 85
}
print("Student Dictionary:", student)
print("Name:", student["name"])
print("Age:", student["age"])
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())
student["city"] = "Ahmedabad"
print("After adding city:", student)
student["marks"] = 90
print("After updating marks:", student)
student.pop("age")
print("After removing age:", student)X
print("\nDictionary Iteration:")
for key, value in student.items():
    print(key, ":", value)
