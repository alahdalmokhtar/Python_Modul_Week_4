import os
import json
from datetime import datetime,timedelta
from Book_transactions import load_books,save_books
import zamen
file_path = 'members.json'
book_path = 'kitap.json'
transaction_id=0
global borrow_date
# Check if the file exists, if not create it with an empty dictionary
if not os.path.exists(book_path):
    with open(book_path, 'w') as file:
        json.dump({}, file)

       
def read_json_file(file_path):
    """Read JSON file and return the data"""
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def load_members():
    """Load all members from the JSON file"""
    members = read_json_file(file_path)
    return members
def load_members():
    try:
        with open('members.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
def load_user():
    try:
        with open('user.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_transactions(transactions):
    with open('transactions.json', 'w') as f:
        json.dump(transactions, f)
        
    print("✅ Transactions saved successfully!")

def save_members(members):
    """Save members to the JSON file"""
    with open(file_path, 'w') as file:
        json.dump(members, file, indent=4)
    print("✅ Members saved successfully!")

def load_members():
    """Load all members from the JSON file"""
    members_file_path = 'members.json'
    if os.path.exists(members_file_path):
        try:
            with open(members_file_path, 'r') as file:
                members = json.load(file)
            return members
        except json.JSONDecodeError:
            print("❌ Error: Failed to decode JSON data.")
            return {}
    else:
        print("❌ Error: Members file does not exist.")
        return {}
def add_member():
    """Add a new member to the library"""
    print("\n--- Add New Member ---")
    
    member_id = input("Member ID: ")
    name = input("Name: ")
    email = input("Email: ")
    tel=input("enter telefoon number :")
    adres=input("enter het adres  :")
    
    # Load existing members first
    members = load_members()
    
    # Check if member ID already exists
    if member_id in members:
        print(f"❌ Member with ID '{member_id}' already exists!")
        return
    
    # Add new member
    members[member_id] = {
        'name': name,
        'email': email,
        'tel':tel,
        'adres':adres
    }
    
    # Save all members (including the new one)
    save_members(members)
    print(f"\n✅ Member '{name}' added successfully!")



def view_members():
    """View all members in the library"""
    print("\n--- View All Members ---")
    
    # Load all members
    members = load_members()
    
    if not members:
        print("❌ No members found!")
        return
    print("\n" + " ----- Members Details ---- :".center(100))
    print("\n{:<10} {:<30} {:<20} {:<15} {:<20}".format("Member ID", "Name", "Email", "Tel", "Address"))
    print("-" * 95)
    # Print all members1

    #print(f"{member_id:<10} {members['name']:<30} {members['email']:<15}")
    for member_id, member in members.items():
         
        print(f"{member_id:<10} "
      f"{str(member.get('name', '')):<30} "
      f"{str(member.get('email', '')):<20} "
      f"{str(member.get('tel', '')):<15} "
      f"{str(member.get('adres', '')):<20}")
        #print("-" * 10)
       
    print("-" * 95)
   
    print("total members:".center(30), len(members))
    print("\n--- End of Member List ---")
    

def delete_members():
    """Delete a member from the library"""
    print("\n--- Delete Member ---")
    
    # Load all members
    members = load_members()
    
    if not members:
        print("❌ No members found!")
        return
    
    member_id = input("Enter the Member ID to delete: ")
    
    # Check if member ID exists
    if member_id in members:
        del members[member_id]
        save_members(members)
        print(f"✅ Member '{member_id}' deleted successfully!")
    else:
        print(f"❌ Member ID '{member_id}' not found!")

def update_members():
    """Update member details"""
    print("\n--- Update Member ---")
    
    # Load all members
    members = load_members()
    
    if not members:
        print("❌ No members found!")
        return
    
    member_id = input("Enter the Member ID to update: ")
    
    # Check if member ID exists
    if member_id in members:
        name = input("New Name (leave blank to keep current): ")
        email = input("New Email (leave blank to keep current): ")

        tel=input("New telefoon number (leave blank to keep current): ")
        adres=input("New adres (leave blank to keep current): ")
        
        if name:
            members[member_id]['name'] = name
        if email:
            members[member_id]['email'] = email
        if tel:
            members[member_id]['tel'] = tel
        if adres:
            members[member_id]['adres'] = adres
    
        save_members(members)
        print(f"✅ Member '{member_id}' updated successfully!")
    else:
        print(f"❌ Member ID '{member_id}' not found!")

def search_members():
    """Search for a member by ID or name"""
    print("\n--- Search Member ---")
    
    # Load all members
    members = load_members()
    
    if not members:
        print("❌ No members found!")
        return
    
    search_term = input("Enter Member ID or Name to search: ")
    
    # Search for the member
    found_members = {k: v for k, v in members.items() if search_term in k or search_term in v['name']}
    
    if found_members:
        print("\n" + " ----- Members Details ---- :".center(100))
        print("\n{:<10} {:<30}{15}{15} {:<15}".format("member_id", "name", "email","tel","adres"))
        print("-" * 85)
        for member_id, member in found_members.items():
            print(f"{member_id:<10} {member['name']:<30} {member['email']:<15} {member['tel']:<15} {member['adres']:<15}")
        print("-" * 85)
    else:
        print(f"❌ No members found with ID or Name '{search_term}'!")

def borrow_book():
    """Borrow a book"""
    print("\n--- Borrow Book ---")
    
    book_name = input("Book title: ")
    member_id = input("Member ID: ")
    
    # Load existing books first
    books = load_books()
    members=load_members()
    transactions=load_transactions()
    borrow_date= (datetime.now()).strftime("%Y-%m-%d %H:%M:%S")
    # Check if book exists
    if book_name not in books:
        print(f"❌ Book '{book_name}' does not exist!")
        return
   
    # Check if member ID exists
    if member_id not in members:
        print(f"❌ Member with ID '{member_id}' does not exist!")
        return
    book = books[book_name]
    member = members[member_id]
    # Add new transaction for borrowing the book
    add_transaction(book_name,member_id)
         
    # Load existing members first
    #members = load_members()

    data={
        "member_id": member_id,
        "member_name": member.get('name', ''),
        "member_tel": member.get('tel', ''),
        "member_adres": member.get('adres', ''),
        "book_barcode": book.get('barcode', ''),
        "book_name": book.get('book_name', ''),
        "book_author": book.get('author', ''),
        "book_publisher": book.get('publisher', ''),
        "book_price": book.get('price', ''),
        "book_language": book.get('language', ''),
        "borrow_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "return_date": (datetime.now() + timedelta(days=14)).strftime("%Y-%m-%d")
    }
    zamen.get_data(data)
    ''' if book_name not in transactions:
        print(f"❌ Book '{book_name}' does not exist!")
        return
    '''
    del books[book_name]  # Remove the book from the available list
    save_books(books)  # Save the updated book list 
    print(f"\n✅ Book '{book_name}' borrowed successfully!")
   # time.get_data(member_id,name,tel,adres,barcode,language,price,book_name,publisher,author)


def return_book():
    """Return a book"""
    file_user="user.json"
    with open (file_user,'r') as f:
        user_data=json.load(f)
 
    print("--- Return Book ---")
    #global borrow_date
    book_name = input("Book title: ")
    member_id = input("Member ID: ")
    
    # Load existing books first
    #transaction = load_transactions()
    users=load_user()
    book=load_books()
    add_transaction(book_name,member_id)

    if book_name not in users:
        print(f"Book '{book_name}' does not exist!")
    for bok in user_data:
       if book_name ==bok['book_name']:
           add_transaction(book_name,member_id)
           print("\n--- Return Book ---")
          # borrow_date=data['borrow_date']
           return_date=bok['return_date']
           book[book_name] ={
       
        'barcode':bok['book_barcode'],
        'language': bok['book_language'],
        'price': bok['book_price'],
        'book_name': book_name,
        'publisher': bok['book_publisher'],
        'author': bok['book_author']
    }
        
                 
    # Add new transaction for returning the book
    #add_transaction(book_name,member_id) 

    #barcode=input("the  new barcode : ")

    # Add new transaction
  
   
    #global borrow_date
   
    
    # Load existing books first
    transaction = load_transactions()
    #book=load_books()

    # Add new transaction for returning the book
       

    #barcode=input("the  new barcode : ")
    # Add new transaction
      
    save_books(book)
    print(f"\n✅ Book '{book_name}' returned successfully!")

def view_transactions():
    """View all transactions in the library"""
    print("\n--- View All Transactions ---")
    
    # Load all transactions
    transactions = load_transactions()
    
    if not transactions:
        print("❌ No transactions found!")
        return
    
    print("\n" + " ----- Transactions Details ---- :".center(100))
    print("\n{:<10} {:<30} {:<15} {:<15}{15}".format("Transaction ID", "Member ID", "Book Name", "Date", "Time Return"))	
    print("-" * 85)
    
    # Print all transactions
    for transaction in transactions:
         print(f"{str(transaction.get('id', '')):<10} "
          f"{str(transaction.get('member_id', '')):<30} "
          f"{str(transaction.get('book_name', '')):<15} "
          f"{str(transaction.get('date', '')):<15} "
          f"{str(transaction.get('time_return', '')):<15}")
          #print(f"{transaction['id']:<10} {transaction['member_id']:<30} {transaction['book_name']:<15} {transaction['date']:<15}  {transaction['time_return']:<15}")
       
    print("-" * 65)
    print("total transactions:".center(30), len(transactions))
    print("\n--- End of Transaction List ---")

def load_transactions():
    """Load all transactions from the JSON file"""
    transactions_file_path = 'transactions.json'
    if os.path.exists(transactions_file_path):
        try:
            with open(transactions_file_path, 'r') as file:
                transactions = json.load(file)
            return transactions
        except json.JSONDecodeError:
            print("❌ Error: Failed to decode JSON data.")
            return {}
    else:
        print("❌ Error: Transactions file does not exist.")
        return {}

   
def add_transaction(book_name,member_id):
    """Add a new transaction"""
    print("\n--- Add New Transaction ---")
    global transaction_id
    #transaction_id = input("Transaction ID: ")
    #book_name = input("Book title: ")
    #member_id = input("Member ID: ")
    date = datetime.now().strftime("%Y-%m-%d %H:%M") # e.g., '2025-05-01'
    time_return = (datetime.now() + timedelta(days=14)).strftime("%Y-%m-%d") # na twee weken
    # Validate date and time format
    
    
    # Load existing transactions first
    transactions = load_transactions()
    count1=len(transactions)
    if count1==0:
        transaction_id=1
    else:
        transaction_id = transactions[-1]['id'] + 1 # Auto-generate a unique ID
   # transaction_id +=1
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
        'date': date,
        'time_return': time_return.format()

    })
    
    # Save all transactions (including the new one)
    save_transactions(transactions)
    
    print(f"\n✅ Transaction '{transaction_id}' added successfully!")


def save_transactions(transactions):
    """Save transactions to the JSON file"""
    with open('transactions.json', 'w') as file:
        json.dump(transactions, file, indent=4)
    print("✅ Transactions saved successfully!")

def main():
    # Load all members
    members = load_members()
    print(f"\nWelcome! Loaded {len(members)} members from the library.")
if __name__ == "__main__":
    main()
    # Your main menu logic would go here
    #


def add_members():
    while True:
        print("-" * 100)
        print("\n" + "Welcome to Members managements".center(100))
        print("\n")
        print("1. Add Members ")
        print("2. Delete Members")
        print("3. Update Members ")
        print("4. Search Members")
        print("5. View All Members")
        print("6. View All Transactions")
        print("7. Lend a book")
        print("8. Return a book")
        print("9. Exit")
        print("-" * 100)
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_member()
            # Add more book transaction options here
            
        elif choice == '2':
            delete_members()
        elif choice == '3':
            update_members()
        elif choice == '4':
            search_members()
        elif choice == '5':
            view_members()
        elif choice == '6':
            view_transactions()
        elif choice == '7':
            borrow_book()
            # Implement lend a book functionality here
        elif choice == '8':
            return_book()
            # Implement return a book functionality here
    
        elif choice == '9':
            print("are you sure you want to exit? (y/n)")
            confirm = input("Enter your choice: ")
            if confirm.lower() == 'y':
               print("Exiting the program.")
               break
            else:
                print("Returning to the main menu.")   
 
    
    # Your main menu logic would go here

    