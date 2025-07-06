students = [
    ("Laziz",["Fizika","Matematika"]),
    ("Laylo",["Ingliz tili"]),
    ("Rashid",["Matematika","Informatika"])
    ]
subject = input()

counter = 0
for student in students:
    if subject in student[1]:
        counter += 1
        print(counter)
        