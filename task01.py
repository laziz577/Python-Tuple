people: list[tuple[str,int]] = [
    ("Ali", 24),
      ("Laylo", 30),
        ("Jasur", 19)]

oldest_person = people[0]
for person in people:
    if person[1] > oldest_person[1]:
        oldest_person = person
print(oldest_person)
        