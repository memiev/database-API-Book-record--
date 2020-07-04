"""
Concerned with storing and retrieving books  form a CSV file
format of the CSV:

name,author,read\n
name,author,read\n
name,author,read\n
name,author,read\n
"""
# Целия код тук се нарича "interface" той крие цялата комплекстност и не пречи в main фаила.

books_file = "books.txt"


def add_book(name, author):
    with open(books_file, mode="a") as file:  # "a" stands for append
        file.write(f"{name},{author},{'0'}\n")


def get_all_books():
    with open(books_file, "r") as file:
        lines = [line.strip().split(",") for line in file.readlines()]  # lists with sub lists
        books = [
            {"name": line[0], "author": line[1], "read": line[2]}
            for line in lines
        ]
    return books


def mark_book_as_read(book_name):
    books = get_all_books()  #
    for book in books:
        if book["name"] == book_name:
            book["read"] = "1"
    _save_all_books(books)


def _save_all_books(books):
    with open(books_file, mode="w") as file:
        for book in books:
            file.write(f"{book['name']},{book['author']},{book['read']}\n")


def delete_book(book_name):
    books = get_all_books()
    books = [book for book in books if book["name"] != book_name]
    _save_all_books(books)


"""
Concerned with storing and retrieving books  form a list.
in-memory DATABASE not SQL
"""

# books = []
#
#
# def prompt_add_book(book_name, book_author):
#     books.append(
#         {
#             "name": book_name,
#             "author": book_author,
#             "read": False
#         }
#     )
#
#
# def list_books():
#     for book in books:
#         check = "read" if book["read"] else "unread"
#         print(f"'{book['name']}' by {book['author']}, status: {check} ")
#
#
# def prompt_read(book_name):
#     for book in books:
#         if book["name"] == book_name and book["read"] is False:
#             book["read"] = True
#
#
# def delete_book(book_name):
#     global books
#     books = [book for book in books if book["name"] != book_name]
