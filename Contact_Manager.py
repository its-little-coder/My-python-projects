import sqlite3

conn = sqlite3.connect("contacts.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS contacts (
    name TEXT,
    phone TEXT,
    birthday TEXT
)
""")
conn.commit()
#add contact
def add_contact():
    name = input("name: ")
    phone = input("phone no.: ")
    birthday = input("dob: ")
    cursor.execute("INSERT INTO contacts (name, phone, birthday) VALUES (?, ?, ?)", (name, phone, birthday))
    conn.commit()
#view contact
def view_contacts():
    cursor.execute("SELECT * FROM contacts")
    results = cursor.fetchall()
    for row in results:
        print(row)
#full version
while True:
    print("\n1. Add contacts")
    print("2. View contacts")
    print("3. Exit")
    choice = input("choose one option 1, 2, 3: ")
    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        out = input("are you sure? y/n: ")
        if out == "y":
            break
        else:
            print("ok")
    else:
        print("invalid choice")
conn.close()

