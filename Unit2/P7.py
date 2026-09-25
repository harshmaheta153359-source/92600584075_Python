numbers = [1,2,3,4,5,6]

squares = [x*x for x in numbers]

print("List comprehension:")
print(squares)

dictionary = {x*x for x in numbers}
print("\nDictionary Comprehension:\n",dictionary)


even_numbers = {x for x in numbers if x % 2 == 0}
print("\nSet Comprehension:")
print(even_numbers)
