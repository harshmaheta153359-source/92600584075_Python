numbers = [10, 20, 30, 40, 50]
print('Orignal list: ',numbers)

print("First element:", numbers[0])
print("Last element:", numbers[-1])

print("First three elements:", numbers[0:3])
print("Last three elements:", numbers[2:])

numbers.append(60)
print("After adding 60:", numbers)

squares = [x * x for x in numbers]
print("Squares using list comprehension:", squares)
