# Hartland Library Management Console
# Student: Federico Mossa | ID: 2314622
# Purpose: Manage books in a small community library system (add, search, borrow, return)

import datetime  # For validating the publication year

# Storage for all books; each book is a dictionary stored inside this list
catalogue = []

# Display the main menu of options
def show_menu():
    print("\nLibrary Menu:")
    print("1. Add a Book")
    print("2. Search for a Book")
    print("3. View All Books")
    print("4. Borrow a Book")
    print("5. Return a Book")
    print("6. Exit")

# Add a new book to the catalogue
def add_book():
    print("\nAdding a New Book...")
    try:
        book_id = input("Enter Book ID (numbers only): ").strip()
        if not book_id.isdigit():
            print("Book ID must contain only numbers.")
            return

        # Prevent duplicate IDs
        for book in catalogue:
            if book['id'] == book_id:
                print("This ID is already in use.")
                return

        title = input("Enter Book Title: ").strip()
        if not title:
            print("Book title cannot be left blank.")
            return

        author = input("Enter Author Name: ").strip()
        if not author:
            print("Author name is required.")
            return

        # Optional warning if same title and author are already recorded
        for book in catalogue:
            if book['title'].lower() == title.lower() and book['author'].lower() == author.lower():
                print("Note: A book with the same title and author already exists.")

        year_input = input("Enter Publication Year: ").strip()
        try:
            year = int(year_input)
            current_year = datetime.datetime.now().year
            if year < 1450 or year > current_year:
                print(f"Year must be between 1450 and {current_year}.")
                return
        except ValueError:
            print("Please enter a valid number for the year.")
            return

        # Save the book
        new_book = {
            'id': book_id,
            'title': title,
            'author': author,
            'year': year,
            'available': True
        }

        catalogue.append(new_book)
        print("Book added successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")

# Search for books by title or author
def search_books():
    print("\nSearch for a Book")
    try:
        keyword = input("Enter title or author to search: ").strip().lower()
        if not keyword:
            print("Search cannot be empty.")
            return

        matches = [book for book in catalogue if keyword in book['title'].lower() or keyword in book['author'].lower()]

        if matches:
            print(f"{len(matches)} book(s) found:")
            for book in matches:
                display_book(book)
        else:
            print("No matching books found.")

    except Exception as e:
        print(f"Search error: {e}")

# Display details of a book
def display_book(book):
    status = "Available" if book['available'] else "Checked Out"
    print(f"ID: {book['id']}, Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, Status: {status}")

# Show all books in the catalogue
def view_all_books():
    print("\nComplete Book List:")
    if not catalogue:
        print("No books in the catalogue.")
        return

    try:
        for book in catalogue:
            display_book(book)
    except Exception as e:
        print(f"Display error: {e}")

# Borrow a book if it's available
def borrow_book():
    print("\nBorrow a Book")
    try:
        book_id = input("Enter the Book ID: ").strip()
        if not book_id.isdigit():
            print("Book ID must be numeric.")
            return

        found = False
        for book in catalogue:
            if book['id'] == book_id:
                found = True
                if book['available']:
                    book['available'] = False
                    print(f"Book '{book['title']}' has been borrowed.")
                else:
                    print("This book is already borrowed.")
                break

        if not found:
            print("No book with that ID was found.")

    except Exception as e:
        print(f"Borrow error: {e}")

# Return a borrowed book
def return_book():
    print("\nReturn a Book")
    try:
        book_id = input("Enter the Book ID: ").strip()
        if not book_id.isdigit():
            print("Book ID must be numeric.")
            return

        found = False
        for book in catalogue:
            if book['id'] == book_id:
                found = True
                if not book['available']:
                    book['available'] = True
                    print(f"Book '{book['title']}' has been returned.")
                else:
                    print("This book was not borrowed.")
                break

        if not found:
            print("No book with that ID was found.")

    except Exception as e:
        print(f"Return error: {e}")

# Run the system until the user exits
def run_system():
    while True:
        try:
            show_menu()
            choice = input("Select an option (1–6): ").strip()

            if choice == '1':
                add_book()
            elif choice == '2':
                search_books()
            elif choice == '3':
                view_all_books()
            elif choice == '4':
                borrow_book()
            elif choice == '5':
                return_book()
            elif choice == '6':
                print("Exiting program. Goodbye.")
                break
            else:
                print("Invalid input. Please choose a number from 1 to 6.")

        except KeyboardInterrupt:
            print("\nProgram interrupted. Exiting safely.")
            break
        except Exception as e:
            print(f"Unexpected error: {e}")

# Run the system if this script is executed directly
if __name__ == "__main__":
    run_system()
