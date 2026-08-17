numbers = (10, 20, 30, 40, 50)

print("Tuple:", numbers)
print("First element:", numbers[0])
print("Last element:", numbers[-1])
print("Tuple slicing:", numbers[1:4])
print("Length of tuple:", len(numbers))


# Set
A = {10, 20, 30, 40}
B = {30, 40, 50, 60}

print("\nSet A:", A)
print("Set B:", B)

print("Union:", A | B)
print("Intersection:", A & B)
print("Difference:", A - B)

A.add(70)
print("After adding 70:", A)

A.remove(20)
print("After removing 20:", A)
