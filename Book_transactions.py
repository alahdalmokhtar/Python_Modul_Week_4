import json
import os
import json
import os

file_path = 'kitap.json'

def load_books():
    """Load all books from the JSON file"""
    if os.path.exists(file_path):
        try:
            with open(file_path, 'r') as file:
                return json.load(file)
        except (json.JSONDecodeError, FileNotFoundError):
            # If file is empty or invalid, return empty dict
            return {}
    return {}
def view_books():
    """View all books in the library"""
    books = load_books()
    if not books:
        print("No books available.")
        return

    print("\n" + " ----- All Book ---- :".center(100))
    print("\n{:<10} {:<30} {:<15} {:<15} {:<15} {:<15}".format("Barcode", "Book Title", "Language", "Price", "Publisher", "Author"))
    print("-" * 100)

    
    for book_name, details in books.items():
        print(f"{details['barcode']:<10} {details['book_name']:<30} {details['language']:<15} {details['price']:<15} {details['publisher']:<15} {details['author']:<15}")
        #print("-" * 10)
        
    print("\n Total books available:", len(books))
def view_transactions():
    """View all transactions"""
    transactions = load_transactions()
    if not transactions:
        print("No transactions available.")
        return
    
    print("\n--- All Transactions ---")
    print("\n{:<10} {:<30} {:<15} {:<15}".format("Transaction ID", "Book Title", "Member ID", "Date"))


    for transaction in transactions:
        print(f"{transaction['id']:<10} {transaction['book_name']:<30} {transaction['member_id']:<15} {transaction['date']:<15}")
        #print("-" * 10)

    print("\n Total transactions:", len(transactions))

def add_transaction():
    """Add a new transaction"""
    print("\n--- Add New Transaction ---")
    
    transaction_id = input("Transaction ID: ")
    book_name = input("Book title: ")
    member_id = input("Member ID: ")
    date = input("Date (YYYY-MM-DD): ")
    
    # Load existing transactions first
    transactions = load_transactions()
    
    # Check if transaction already exists
    for transaction in transactions:
        if transaction['id'] == transaction_id:
            print(f"❌ Transaction ID '{transaction_id}' already exists!")
            return
    
    # Add new transaction
    transactions.append({
        'id': transaction_id,
        'book_name': book_name,
        'member_id': member_id,
        'date': date
    })
    
    # Save all transactions (including the new one)
    save_transactions(transactions)
    print(f"\n✅ Transaction '{transaction_id}' added successfully!")

def delete_book():
    """Delete a book"""
    print("\n--- Delete Book ---")
    
    book_name = input("Book title: ")
    
    # Load existing books first
    books = load_books()
    
    # Check if book exists
    if book_name not in books:
        print(f"❌ Book '{book_name}' does not exist!")
        return
    
    # Delete the book
    del books[book_name]
    
    # Save all books (excluding the deleted one)
    save_books(books)
    print(f"\n✅ Book '{book_name}' deleted successfully!")

def update_book():
    """Update an existing book"""
    print("\n--- Update Book ---")
    
    book_name = input("Book title to update: ")
    book_bardcode = input("Book barcode to update: ")

    books = load_books()
    

    if book_name not in books:
        print(f"❌ Book '{book_name}' does not exist!")
        return
    '''if book_bardcode in [book['barcode'] for book in books.values()]:
        print(f"❌ Book with barcode '{book_bardcode}' already exists!")
        return 
    '''

    new_barcode = input("New Barcode: ")
    new_language = input("New Language: ")
    new_price = input("New Price: ")
    new_publisher = input("New Publisher: ")
    new_author = input("New Author: ")
    

    books[book_name].update({
        'barcode': new_barcode,
        'language': new_language,
        'price': new_price,
        'publisher': new_publisher,
        'author': new_author
    })
    

    save_books(books)
    print(f"\n✅ Book '{book_name}' updated successfully!")
    view_books()

def search_book():
    """Search for a book by title"""
    print("\n--- Search Book ---")
    
    book_name = input("Enter book title to search: ")
    

    books = load_books()
    
    if book_name in books:
        print(f"✅ Book found: {book_name}")
        print("\n" + " ----- Book Details you are searched ---- :".center(100))
        print("\n{:<10} {:<30} {:<15} {:<15} {:<15} {:<15}".format("Barcode", "Book Title", "Language", "Price", "Publisher", "Author"))
        print("-" * 100)
        print(f"{books[book_name]['barcode']:<10} {books[book_name]['book_name']:<30} {books[book_name]['language']:<15} {books[book_name]['price']:<15} {books[book_name]['publisher']:<15} {books[book_name]['author']:<15}")
       # print(f"details: {books[book_name]}")
    else:
        print(f"❌ Book '{book_name}' does not exist!")

def load_transactions():
    """Load all transactions from the JSON file"""
    transactions_file_path = 'transactions.json'
    if os.path.exists(transactions_file_path):
        try:
            with open(transactions_file_path, 'r') as file:
                return json.load(file)
        except (json.JSONDecodeError, FileNotFoundError):
            # If file is empty or invalid, return empty list
            return []
    return []
def save_transactions(transactions):
    """Save all transactions to the JSON file"""
    transactions_file_path = 'transactions.json'
    with open(transactions_file_path, 'w') as file:
        json.dump(transactions, file, indent=4)

def save_books(books):
    """Save all books to the JSON file"""
    with open(file_path, 'w') as file:
        json.dump(books, file, indent=4)

def add_new_books():
    """Add a new book transaction"""
    print("\n--- Add New Book ---")
    
    barcode = input("Barcode: ")
    language = input("Language: ")
    price = input("Price: ")
    book_name = input("Book title (or 'exit' to cancel): ")
    if book_name.lower() == 'exit':
        return
    publisher = input("Publisher: ")
    author = input("Author: ")
    
    # Load existing books first
    books = load_books()
    
    # Check if barcode for book already exists
    if barcode in [book['barcode'] for book in books.values()]:
        print(f"❌ Book with barcode '{barcode}' already exists!")
        return
    
    # Add new book
    books[book_name] = {
        'barcode': barcode,
        'language': language,
        'price': price,
        'book_name': book_name,
        'publisher': publisher,
        'author': author
    }
    
    # Save all books (including the new one)
    save_books(books)
    print(f"\n✅ Book '{book_name}' added successfully!")

def main():
    # Load all books
    books = load_books()
    print(f"\nWelcome! Loaded {len(books)} books from the library.")
    
    # Your main menu logic would go here
    add_books()

if __name__ == "__main__":
    main()

def add_books():
    
    while True:
        print("-" * 100)
        print("\n" + "Welcome to Books managements".center(100))
        print("\n")
        print("1. Add Book Transactions")
        print("2. Delete  Books ")
        print("3. Update Book Transactions")
        print("4. Search Book Transactions")
        print("5. View All Books")
        print("6. View All Transactions")
        print("7. Exit")
        print("-" * 100)
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_new_books()
            # Add more book transaction options here
            
        elif choice == '2':
            delete_book()
        elif choice == '3':
            update_book()
        elif choice == '4':
            search_book()
        elif choice == '5':
            view_books()
        elif choice == '6':
            view_transactions()
        elif choice == '7':
            print("are you sure you want to exit? (y/n)")
            confirm = input("Enter your choice: ")
            if confirm.lower() == 'y':
               print("Exiting the program.")
               break
            else:
                print("Returning to the main menu.")  
 
