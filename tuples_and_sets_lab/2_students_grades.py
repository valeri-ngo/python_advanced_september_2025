num = int(input())

student_record = {}

for _ in range(num):
    info = input().split()
    name = info[0]
    grade = float(info[1])

    if name not in student_record:
        student_record[name] = []
    student_record[name].append(grade)

for name, grades in student_record.items():
    avg_grade = sum(grades) / len(grades)
    grades_as_str = [f"{ele:.2f}" for ele in grades]
    print(f"{name} -> {' '.join(grades_as_str)} (avg: {avg_grade:.2f})")