import Member_Transactions
import time
import Book_transactions
import _json
import json
import os



def read_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def load_books():
    books = read_json_file('kitap.json')
    return books

def load_members():
    members= read_json_file('members.json')
    return members
def load_transactions():
    transactions = read_json_file('transactions.json')
    return transactions


def main():
    #load json files
    data=read_json_file('kitap.json')
    print(f"\nWelcome! Loaded {len(data)} book from Libarary.")
while True:
    print("-" * 100)
    print("\n" + "welcome to our Library management system".center(100))
    print("\n")
    print("1. book_transactions ")
    print("2. member_transactions")
    print("0. exit")
    print("-" * 100)
    choice = input("Enter your choice: ")
    if choice == '1':
        print ("Book Transactions")
        print("1. Add a new book")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. View all books")
        print("5. View all transactions")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            Book_transactions.add_books()
        elif choice == '2':
            Book_transactions.borrow_book()
        elif choice == '3':
            Book_transactions.return_book()
        elif choice == '4':
            Book_transactions.view_books()
        elif choice == '5':
            Book_transactions.view_transactions()
        elif choice == '6':
            print("Exiting the program.")
            break
        Book_transactions.load_books()
        Book_transactions.view_books()
        Book_transactions.view_transactions()

    elif choice == '2':
        print("Member Transactions")
        Member_Transactions.add_members()
        Member_Transactions.view_members()
    elif choice == '0':
        print("are you sure you want to exit? (y/n)")
        confirm = input("Enter your choice: ")
        if confirm.lower() == 'y':
            print("Exiting the program.")
            break
        else:
            print("Returning to the main menu.")  
'''
        print("\n1. Add a new book")
    print("2. Add a new member")
    print("3. Borrow a book")
    print("4. Return a book")
    print("5. View all books")
    print("6. View all members")
    print("7. View all transactions")
    print("8. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        Book_transactions.add_book()
    elif choice == '2':
        Member_Transactions.add_member()
    elif choice == '3':
        Book_transactions.borrow_book()
    elif choice == '4':
        Book_transactions.return_book()
    elif choice == '5':
        Book_transactions.view_books()
    elif choice == '6':
        Member_Transactions.view_members()
    elif choice == '7':
        Member_Transactions.view_transactions()
    elif choice == '8':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
    pass
'''
if __name__ == "__main__":
    main()