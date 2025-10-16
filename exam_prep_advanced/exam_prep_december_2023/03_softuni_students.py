def softuni_students(*args, **kwargs):
    course_by_id = dict(kwargs)

    valid = []
    invalid = []

    for course_id, username in args:
        if course_id in course_by_id:
            valid.append((username, course_by_id[course_id]))
        else:
            invalid.append(username)

    valid.sort(key=lambda x: x[0])
    invalid.sort()

    lines = []
    for username, course in valid:
        lines.append(f"*** A student with the username {username} has successfully finished the course {course}!")
    if invalid:
        lines.append(f"!!! Invalid course students: {', '.join(invalid)}")

    return '\n'.join(lines)


print(softuni_students(
    ('id_1', 'Kaloyan9905'),
    id_1='Python Web Framework',
))
print()
print(softuni_students(
    ('id_7', 'Silvester1'),
    ('id_32', 'Katq21'),
    ('id_7', 'The programmer'),
    id_76='Spring Fundamentals',
    id_7='Spring Advanced',
))
print()
print(softuni_students(
    ('id_22', 'Programmingkitten'),
    ('id_11', 'MitkoTheDark'),
    ('id_321', 'Bobosa253'),
    ('id_08', 'KrasimirAtanasov'),
    ('id_32', 'DaniBG'),
    id_321='HTML & CSS',
    id_22='Machine Learning',
    id_08='JS Advanced',
))
