import backup

def remove_book(book_list):
    search_key = input("Enter title of a book to search and delete: ")

    for idx, book in enumerate(book_list):
        if (search_key in book["title"]):
            print(f"index: {idx+1} !!!\n{book["title"]} - {book["authors"]} - {book["isbn"]} - {book["publishing_year"]} - {book["price"]} - {book["quantity"]}")

    selected_idx = int(input("Enter a book index to remove: "))

    if (selected_idx < len(book_list)):
        print("Invalid index (-_-)")
    else:
        book_list.pop(selected_idx-1)
        print("Book removed successfully!!!")

        backup.backup_book(book_list)
    
    return book_list