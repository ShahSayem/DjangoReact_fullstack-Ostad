import backup

def add_book(book_list):
    title = input("Enter title: ")
    try:
        num = int(input("Enter number of authors: "))
    except ValueError:
        print("Number of authors should be integer value (-_-)")

    authors = []

    for i in range(num):
        name = input(f"Enter author name {i+1}: ")
        authors.append(name)

    isbn = input("Enter ISBN: ")
    try:
        publishing_year = int(input("Enter publisihing year: "))
        price = float(input("Enter price: "))
        quantity = int(input("Enter quantity: "))
    except ValueError:
        print("Inputs of publisihing year, quantity should be integer value (-_-)")
        print("Input of price should be floating value (-_-)")

    book_takers = []

    new_book = {
        "title": title,
        "authors": authors,
        "isbn": isbn,
        "publishing_year": publishing_year,
        "price": price,
        "quantity": quantity,
        "book_takers": book_takers
    }

    
    book_list.append(new_book)

    print("Book added successfully!!!")

    backup.backup_book(book_list)

    return book_list