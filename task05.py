numbers = (3, 6, 7, 8, 10, 11)
new_number = []
for i in numbers:
    if i % 2 == 0: 
        new_number.append(i)
        a = tuple(new_number)
print(a)
