import random

numbers = []
for i in range(100):
    numbers.append(random.randint(100, 900))

print(numbers)

odd = 0
even = 0
prime = 0

for n in numbers:
    if n % 2 == 0:
        even += 1
    else:
        odd += 1

    count = 0
    for d in range(2, n):
        if n % d == 0:
            count += 1
            break
    if count == 0:
        prime += 1

print("Odd numbers =", odd)
print("Even numbers =", even)
print("Prime numbers =", prime)
