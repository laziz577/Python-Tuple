emails = (
    ("Ali", "ali@gmail.com"),
    ("Vali", "vali@yandex.ru"),
    ("G'ani", "sami@mail.ru")
    )

domains = []

for email in emails:
    i = email[1].find("@")         
    domain = email[1][i + 1:]      
    domains.append(domain)         

print(domains)
