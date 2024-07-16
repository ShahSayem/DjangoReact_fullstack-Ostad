import add
import view
import search
import remove
import lend
import backup
import restore
import return_book

book_list = []


while(True):
    book_list = restore.restore_book(book_list)

    print("\nMenue:")
    menue_txt = """
    # Your options:
    1. Add Book
    2. View All Books
    3. Search Books (by Title / ISBN)
    4. Search Books (by Author)
    5. Remove Book
    6. Book Lend
    7. View Lended Books and Book Takers
    8. Book Return
    9. Exit
    """

    print(menue_txt)
    choice = input("Enter your choice: ")

    if (choice == "1"):
        book_list = add.add_book(book_list)
    elif (choice == "2"):
        view.view_all_books(book_list)
    elif (choice == "3"):
        search.search_book(book_list)
    elif (choice == "4"):
        search.search_by_author(book_list)
    elif (choice == "5"):
        book_list = remove.remove_book(book_list)    
    elif (choice == "6"):
        book_list = lend.book_lend(book_list)
    elif (choice == "7"):
        view.lended_books_lenders(book_list)  
    elif (choice == "8"):
        book_list = return_book.book_return(book_list)            
    elif (choice == "9"):
        print("Program terminated!!!")
        break
    else:
        print("Invalid choice (-_-)")