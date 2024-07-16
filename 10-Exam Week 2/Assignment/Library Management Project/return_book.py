import backup

def book_return(book_list):
    book_taker = input("Enter the name of book returner: ")
    book_title = input("Enter title of the book: ")

    idx_list = []
    flag = True
    for idx, book in enumerate(book_list):
        if (book_title in book["title"]):
            print(f"index: {idx+1} !!!\n{book["title"]} - {book["authors"]} - {book["isbn"]} - {book["publishing_year"]} - {book["price"]} - {book["quantity"]}")
            flag = False
            idx_list.append(idx)

    if (flag):
        print("No book found in this title (-_-)")
    else:
        selected_idx = int(input("Enter a book index to return: "))

        if (book_taker in book_list[selected_idx-1]["book_takers"] and selected_idx-1 in idx_list):
            book_list[selected_idx-1]["quantity"] += 1
            book_list[selected_idx-1]["book_takers"].remove(book_taker)
            print("Book returned successfully!!!")


            backup.backup_book(book_list)
        else:
            print("Invalid book taker or book index")

        return book_list