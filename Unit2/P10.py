def generate_numbers(n):
    for i in range(1, n + 2):
        yield i

print("Sequence of numbers:")

for num in generate_numbers(10):
    print(num)
