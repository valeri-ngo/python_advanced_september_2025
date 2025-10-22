def classify_books(*args, **kwargs):
    fiction = []
    non_fiction = []

    for genre, title in args:
        if genre == 'fiction':
            fiction.append(title)
        elif genre == 'non_fiction':
            non_fiction.append(title)

    fiction_books = []
    non_fiction_books = []

    for isbn, title in kwargs.items():
        if title in fiction:
            fiction_books.append((isbn, title))
        elif title in non_fiction:
            non_fiction_books.append((isbn, title))

    sorted_fiction_books = sorted(fiction_books, key= lambda kvp: kvp[0])
    sorted_non_fiction_books = sorted(non_fiction_books, key= lambda kvp: kvp[0], reverse= True)

    result = ''

    if fiction_books:
        result += "Fiction Books:\n"
        for isbn, title in sorted_fiction_books:
            result += f"~~~{isbn}#{title}\n"

    if non_fiction_books:
        result += "Non-Fiction Books:\n"
        for isbn, title in sorted_non_fiction_books:
            result += f"***{isbn}#{title}\n"

    return result


print(classify_books(
    ("fiction", "Brave New World"),
    ("non_fiction", "The Art of War"),
    NF3421NN="The Art of War",
    FF1234UU="Brave New World"
))
print()
print(classify_books(
    ("non_fiction", "The Art of War"),
    ("fiction", "The Great Gatsby"),
    ("non_fiction", "A Brief History of Time"),
    ("fiction", "Brave New World"),
    FF1234HH="The Great Gatsby",
    NF3845UU="A Brief History of Time",
    NF3421NN="The Art of War",
    FF1234UU="Brave New World"
))
print()
print(classify_books(
    ("fiction", "Brave New World"),
    ("fiction", "The Catcher in the Rye"),
    ("fiction", "1984"),
    FICCITRZZ="The Catcher in the Rye",
    FIC1984XX="1984",
    FICBNWYYY="Brave New World"
))
print()
print(classify_books(
    ("non_fiction", "Sapiens"),
    ("non_fiction", "Homo Deus"),
    ("non_fiction", "The Selfish Gene"),
    NF123ABC="Sapiens",
    NF987XYZ="Homo Deus",
    NF456DEF="The Selfish Gene"
))
