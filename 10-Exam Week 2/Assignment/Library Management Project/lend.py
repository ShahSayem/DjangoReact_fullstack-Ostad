import backup

def book_lend(book_list):
    book_taker = input("Enter the name of book taker: ")
    book_title = input("Enter title of the book: ")

    flag = True
    for idx, book in enumerate(book_list):
        if (book_title in book["title"]):
            print(f"index: {idx+1} !!!\n{book["title"]} - {book["authors"]} - {book["isbn"]} - {book["publishing_year"]} - {book["price"]} - {book["quantity"]}")
            flag = False

    if (flag):
        print("No book found in this title")
    else:
        selected_idx = int(input("Enter a book index to lend: "))

        if (book_list[selected_idx-1]["quantity"] > 0):
            book_list[selected_idx-1]["quantity"] -= 1
            book_list[selected_idx-1]["book_takers"].append(book_taker)

            print("Book lended successfully!!!")
        else:
            print("Not enough book to lend (-_-)")

        backup.backup_book(book_list)

    return book_list


