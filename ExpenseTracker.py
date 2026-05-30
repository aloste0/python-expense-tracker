import sqlite3

connection = sqlite3.connect("expenses.db")

cursor = connection.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses(
id INTEGER PRIMARY KEY AUTOINCREMENT,
amount INTEGER,
category TEXT,
date TEXT       
)
""")

def insert():
    amount = input("Enter the amount : ")
    category = input("Enter the category : ")
    date = input("Enter the date : dd-mm-yyyy \n")
    cursor.execute(
        "INSERT INTO expenses (amount,category,date) VALUES (?, ?, ?)", (amount,category,date)
    )
    connection.commit()

def display():
    cursor.execute(
        "SELECT * FROM expenses"
    )
    for row in cursor.fetchall():
        print(row)
    connection.commit()

def search_category():
    cat = input("Enter the category : ")
    cursor.execute(
        "SELECT * FROM expenses WHERE category = ?", (cat, )
    )
    for row in cursor.fetchall():
        print(row)
    connection.commit()

def delete():
    index = input("Enter the expense id : ")
    cursor.execute(
        "DELETE FROM expenses WHERE id = ?",(index, )
    )
    connection.commit()

def total_expenses():
    total = 0
    cursor.execute(
        "SELECT amount FROM expenses"
    )
    for i in cursor.fetchall():
        total += i[0]
    connection.commit()
    print(total)

while True:
    choice = input("1- Add an expense\n2- Display all expenses\n3- Search by category\n4- Delete an expense\n5- Total expenses\n6- Exit")
    match choice:
        case "1":
            insert()
        case "2":
            display()
        case "3":
            search_category()
        case "4":
            delete()
        case "5":
            total_expenses()
        case "6":
            break
        case _:
            print("Invalid input")
