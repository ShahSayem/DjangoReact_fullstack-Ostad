def restore_book(book_list):
    #for creating file if not exist
    with open("book_file.csv", "a") as fp:
        pass
    book_list.clear()
    
    with open("book_file.csv", "r") as fp:
        for line in fp.readlines():
            line_list = line.split("-")

            if (len(line_list) > 1):
                book = {
                    "title": line_list[0],
                    "authors": line_list[1],
                    "isbn": line_list[2],
                    "publishing_year": int(line_list[3]),
                    "price": float(line_list[4]),
                    "quantity": int(line_list[5]),
                    "book_takers": line_list[6]
                }

                book_list.append(book)

    return book_list