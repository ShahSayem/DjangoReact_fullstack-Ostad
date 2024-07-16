def restore_contact(contact_book):
    #for creating file if not exist
    with open("contcats.csv", "a") as fp:
        pass
    contact_book.clear()
    
    with open("contcats.csv", "r") as fp:
        for line in fp.readlines():
            line_list = line.split(",")

            if (len(line_list) > 1):
                contact = {
                    "name": line_list[0],
                    "phone": line_list[1],
                    "email": line_list[2]
                }

                contact_book.append(contact)

    return contact_book