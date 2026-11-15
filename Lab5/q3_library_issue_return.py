"""Library record system for adding, issuing, returning, and reporting books."""

library_books = {
    "ISBN101": {"title": "Python Basics", "author": "Rao", "copies": 2, "issued_to": []},
    "ISBN102": {"title": "Data Structures", "author": "Iyer", "copies": 1, "issued_to": []},
    "ISBN103": {"title": "Algorithms", "author": "Rao", "copies": 1, "issued_to": []},
}


def add_book():
    isbn = input("Enter ISBN: ").strip()
    if isbn in library_books:
        additional = int(input("Enter additional copies: "))
        if additional > 0:
            library_books[isbn]["copies"] += additional
            print("Copies updated.")
        else:
            print("Enter a positive number.")
        return

    title = input("Enter book title: ").strip()
    author = input("Enter author: ").strip()
    copies = int(input("Enter number of copies: "))
    if not title or not author:
        print("Book title and author cannot be empty.")
        return
    if copies <= 0:
        print("Copies must be greater than zero.")
        return

    library_books[isbn] = {
        "title": title,
        "author": author,
        "copies": copies,
        "issued_to": [],
    }
    print("Book added.")


def issue_book():
    isbn = input("Enter ISBN: ").strip()
    member_id = input("Enter member ID: ").strip()

    if isbn not in library_books:
        print("Book not found.")
        return

    book_record = library_books[isbn]
    if book_record["copies"] <= 0:
        print("No copies are available.")
        return
    if member_id in book_record["issued_to"]:
        print("This member already has this book.")
        return

    borrowed_count = sum(
        member_id in record["issued_to"]
        for record in library_books.values()
    )
    if borrowed_count >= 2:
        print("A member can hold a maximum of two books.")
        return

    book_record["copies"] -= 1
    book_record["issued_to"].append(member_id)
    print("Book issued successfully.")


def return_book():
    isbn = input("Enter ISBN: ").strip()
    member_id = input("Enter member ID: ").strip()

    if isbn in library_books and member_id in library_books[isbn]["issued_to"]:
        library_books[isbn]["issued_to"].remove(member_id)
        library_books[isbn]["copies"] += 1
        print("Book returned.")
    else:
        print("No matching issued book was found.")


def search_book():
    isbn = input("Enter ISBN: ").strip()
    book_record = library_books.get(isbn)
    if book_record is None:
        print("Book not found.")
    else:
        print(book_record)


def display_library_reports():
    author_name = input("Enter author name: ").strip().lower()
    matching_books = {
        isbn: record["title"]
        for isbn, record in library_books.items()
        if record["author"].lower() == author_name
    }
    print("\nBooks by author:", matching_books)

    borrowed_by_member = {}
    for record in library_books.values():
        for member_id in record["issued_to"]:
            borrowed_by_member.setdefault(member_id, []).append(record["title"])

    multiple_books = {
        member_id: titles
        for member_id, titles in borrowed_by_member.items()
        if len(titles) > 1
    }
    print("\nMembers holding multiple books:", multiple_books)

    out_of_stock = {
        isbn: record["title"]
        for isbn, record in library_books.items()
        if record["copies"] == 0
    }
    print("\nBooks with no available copies:", out_of_stock)

    never_borrowed = {
        isbn: record["title"]
        for isbn, record in library_books.items()
        if not record["issued_to"]
    }
    print("\nBooks never issued:", never_borrowed)


def main():
    while True:
        print("\n--- LIBRARY RECORD SYSTEM ---")
        print("1. Add book")
        print("2. Issue book")
        print("3. Return book")
        print("4. Search book")
        print("5. Reports")
        print("6. Exit")

        option = input("Choose an option: ")
        if option == "1":
            add_book()
        elif option == "2":
            issue_book()
        elif option == "3":
            return_book()
        elif option == "4":
            search_book()
        elif option == "5":
            display_library_reports()
        elif option == "6":
            print("Program closed.")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
