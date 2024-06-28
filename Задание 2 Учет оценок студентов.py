# в задании смутило условие "По определенному предмету", что не соответствует решению.
grades = {}
all_students = int(input("Введите количество студентов "))
for i in range(all_students):
    name = input("Введите имя ")
    grade = int(input("Введите оценку "))
    grades[name]=grade
# print(grades) проверка словаря
avg = float(sum(grades.values())/len(grades))
print(f"Средний балл равен {avg}")
