def view_all_books(book_list):
    for book in book_list:
        print(
            book["title"], 
            book["authors"],
            book["isbn"],
            book["publishing_year"],
            book["price"],
            book["quantity"],
            sep= " | " #for separating with " | "
        )


def lended_books_lenders(book_list):
    for idx, book in enumerate(book_list):
        if (len(book["book_takers"])):
            print(f"index: {idx+1} !!!\n{book["title"]} - {book["isbn"]} - {book["quantity"]} - {book["book_takers"]}")