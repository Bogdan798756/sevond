subjects = []
subject = input("Введи предмет(0-зупинити введення):")
subject=subject.lower()
while subject !="0":
    if subject in subjects:
        print("Цей предмет вже записаний")
    else:
        subjects.append(subject)
    subject=input("Введи предмет(0-зупинити введення):")
    subject=subject.lower()
    subjects.sort()
print("Список предметів:",subjects)
