def backup_book(book_list):
    #for erase to write all entries
    with open("book_file.csv", "wt") as fp:
        pass

    with open("book_file.csv", "a", newline="\n") as fp:
        for book in book_list:
            line = f"{book["title"]}-{book["authors"]}-{book["isbn"]}-{book["publishing_year"]}-{book["price"]}-{book["quantity"]}-{book["book_takers"]}\n"
            fp.write(line)
