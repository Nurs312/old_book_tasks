age = int(input('Enter your age: '))
even = []
odd = []
for num in range(age + 1):
    if (age % 2) == 0:
        if (num % 2) == 0:
            even.append(num)
        print(num)
    else:
        if (num % 2) != 0:
            odd.append(num)
        print(num)# Можно и так: print(even). Но тогда мы получим список.
