numbers = [10,20,30,40]
print("Iterables")

for x in numbers:
    print(x)

it = iter(numbers)
print("\nIterators")
print(next(it))
print(next(it))
print(next(it))
print(next(it))
