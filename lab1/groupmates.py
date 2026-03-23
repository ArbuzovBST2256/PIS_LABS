groupmates = [
    {
        "name": "Элина",
        "group": "БСТ2256",
        "age": 24,
        "marks": [5, 5, 5, 5, 5]
    },
    {
        "name": "Алексей",
        "group": "БСТ2256",
        "age": 24,
        "marks": [4, 4, 5, 4, 4]
    },
    {
        "name": "Владислав",
        "group": "БСТ2256",
        "age": 24,
        "marks": [3, 4, 3, 4, 3]
    },

    {
        "name": "Дмитрий",
        "group": "БСТ2255",
        "age": 22,
        "marks": [4, 5, 4, 4, 5]
    },
    {
        "name": "Ольга",
        "group": "БСТ2255",
        "age": 23,
        "marks": [3, 4, 4, 3, 4]
    },
    {
        "name": "Иван",
        "group": "БСТ2255",
        "age": 21,
        "marks": [5, 5, 4, 5, 5]
    },

    {
        "name": "Мария",
        "group": "БСТ2257",
        "age": 25,
        "marks": [4, 4, 4, 5, 4]
    },
    {
        "name": "Никита",
        "group": "БСТ2257",
        "age": 26,
        "marks": [3, 3, 4, 3, 3]
    },
    {
        "name": "Светлана",
        "group": "БСТ2257",
        "age": 27,
        "marks": [5, 5, 5, 5, 4]
    }
]

def print_students(students):
    print(
        "Имя".ljust(15),
        "Группа".ljust(10),
        "Возраст".ljust(10),
        "Оценки".ljust(20)
    )

    for s in students:
        print(
            s["name"].ljust(15),
            s["group"].ljust(10),
            str(s["age"]).ljust(10),
            str(s["marks"]).ljust(20)
        )

    print()

print_students(groupmates)

def filter_students(students, avg_score):
    result = []

    for student in students:
        avg = sum(student["marks"]) / len(student["marks"])
        if avg >= avg_score:
            result.append(student)

    return result

good_students = filter_students(groupmates, 4.0)
print("Студенты со средним баллом 4.0 и выше:")
print_students(good_students)
