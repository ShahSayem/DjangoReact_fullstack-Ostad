def search_book(book_list):
    search_key = input("Enter title or ISBN of a book to search: ")

    book_set = set()
    flag = False
    for idx, book in enumerate(book_list):
        if (search_key in book["title"]):
            book_set.add(f"index: {idx+1} !!!\n{book["title"]} - {book["authors"]} - {book["isbn"]} - {book["publishing_year"]} - {book["price"]} - {book["quantity"]}")
            flag = True

        if (search_key in book["isbn"]):
            book_set.add(f"index: {idx+1} !!!\n{book["title"]} - {book["authors"]} - {book["isbn"]} - {book["publishing_year"]} - {book["price"]} - {book["quantity"]}")
            flag = True

    if (not flag):
        print("No book found (-_-)")
    else:
        for book in book_set:
            print(book)


def search_by_author(book_list):
    author = input("Enter author of a book to search: ")

    flag = False
    for idx, book in enumerate(book_list):
        if (author in book["authors"]):
            print(f"index: {idx+1} !!!\n{book["title"]} - {book["authors"]} - {book["isbn"]} - {book["publishing_year"]} - {book["price"]} - {book["quantity"]}")
            flag = True

    if (not flag):
        print("No book found (-_-)")