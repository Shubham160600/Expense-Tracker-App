import csv

def add_expense(description, amount):
    with open('expenses.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([description, amount])

def view_expenses():
    with open('expenses.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(f"Description: {row[0]}, Amount: ${row[1]}")

# Example usage
add_expense("Groceries", 50)
view_expenses()
