import os
from datetime import datetime
from collections import defaultdict

EXPENSE_FILE = "expenses.txt"
INCOME_FILE = "income.txt"

def add_income():
    while True:
        date = input("Enter income date (YYYY-MM-DD): ")
        try:
            datetime.strptime(date, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date format. Use YYYY-MM-DD.")

    while True:
        try:
            amount = float(input("Enter income amount (in ₹): "))
            break
        except ValueError:
            print("Invalid amount. Enter a number.")

    source = input("Enter income source (e.g., Salary, Freelance): ")

    with open(INCOME_FILE, "a") as file:
        file.write(f"{date},{amount},{source}\n")

    print(f"₹{amount:.2f} added from '{source}' on {date}.")

def view_income():
    if not os.path.exists(INCOME_FILE):
        print("No income data found.")
        return

    print("Date        | Amount | Source")
    print("-" * 40)

    with open(INCOME_FILE, "r") as file:
        for line in file:
            try:
                date, amount, source = line.strip().split(",")
                print(f"{date} | ₹{amount:<6} | {source}")
            except ValueError:
                continue

def add_expense():
    while True:
        date = input("Enter expense date (YYYY-MM-DD): ")
        try:
            datetime.strptime(date, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date format. Use YYYY-MM-DD.")

    while True:
        try:
            amount = float(input("Enter expense amount (in ₹): "))
            break
        except ValueError:
            print("Invalid amount. Enter a number.")

    category = input("Enter expense category (e.g., Food, Travel, Shopping, Rent, Entertainment, Health, Education, Bills): ").strip()

    if category.lower() == "travel":
        from_location = input("From where (e.g., Home): ")
        to_location = input("To where (e.g., College): ")
        item = f"Travel from {from_location} to {to_location}"
    else:
        item_name = input("Enter item (e.g., Momos, T-Shirt): ")
        place = input("Enter shop/place (e.g., GVK Mall): ")
        item = f"{item_name} at {place}"

    with open(EXPENSE_FILE, "a") as file:
        file.write(f"{date},{amount},{item},{category}\n")

    print(f"₹{amount:.2f} expense added for '{item}' under '{category}' category.")

def view_expenses():
    if not os.path.exists(EXPENSE_FILE):
        print("No expense data found.")
        return

    print("Date        | Amount | Item                          | Category")
    print("-" * 70)

    with open(EXPENSE_FILE, "r") as file:
        for line in file:
            try:
                date, amount, item, category = line.strip().split(",")
                print(f"{date} | ₹{amount:<6} | {item:<30} | {category}")
            except ValueError:
                continue

def show_avg_expenses():
    monthly = defaultdict(lambda: {"total": 0, "days": set()})
    yearly = defaultdict(lambda: {"total": 0, "days": set()})

    if not os.path.exists(EXPENSE_FILE):
        print("No expenses found.")
        return

    with open(EXPENSE_FILE, "r") as file:
        for line in file:
            try:
                date_str, amount, _, _ = line.strip().split(",")
                date = datetime.strptime(date_str, "%Y-%m-%d")
                month = date.strftime("%Y-%m")
                year = date.strftime("%Y")
                monthly[month]["total"] += float(amount)
                monthly[month]["days"].add(date_str)
                yearly[year]["total"] += float(amount)
                yearly[year]["days"].add(date_str)
            except ValueError:
                continue

    print("Monthly Average Daily Spending:")
    for month in sorted(monthly):
        total = monthly[month]["total"]
        days = len(monthly[month]["days"])
        avg = total / days if days else 0
        print(f"- {month}: ₹{avg:.2f} per day (₹{total:.2f} over {days} day(s))")

    print("Yearly Average Daily Spending:")
    for year in sorted(yearly):
        total = yearly[year]["total"]
        days = len(yearly[year]["days"])
        avg = total / days if days else 0
        print(f"- {year}: ₹{avg:.2f} per day (₹{total:.2f} over {days} day(s))")

def show_avg_income():
    if not os.path.exists(INCOME_FILE):
        print("No income records.")
        return

    monthly = defaultdict(float)

    with open(INCOME_FILE, "r") as file:
        for line in file:
            try:
                date_str, amount, _ = line.strip().split(",")
                date = datetime.strptime(date_str, "%Y-%m-%d")
                month = date.strftime("%Y-%m")
                monthly[month] += float(amount)
            except ValueError:
                continue

    if not monthly:
        print("No monthly income data.")
        return

    total_income = sum(monthly.values())
    avg_income = total_income / len(monthly)

    print("Average Monthly Income:")
    for month in sorted(monthly):
        print(f"- {month}: ₹{monthly[month]:.2f}")
    print(f"Average: ₹{avg_income:.2f} over {len(monthly)} month(s)")

def compare_income_vs_expenses():
    income_data = defaultdict(float)
    expense_data = defaultdict(float)

    if os.path.exists(INCOME_FILE):
        with open(INCOME_FILE, "r") as file:
            for line in file:
                try:
                    date_str, amount, _ = line.strip().split(",")
                    month = datetime.strptime(date_str, "%Y-%m-%d").strftime("%Y-%m")
                    income_data[month] += float(amount)
                except ValueError:
                    continue

    if os.path.exists(EXPENSE_FILE):
        with open(EXPENSE_FILE, "r") as file:
            for line in file:
                try:
                    date_str, amount, _, _ = line.strip().split(",")
                    month = datetime.strptime(date_str, "%Y-%m-%d").strftime("%Y-%m")
                    expense_data[month] += float(amount)
                except ValueError:
                    continue

    all_months = sorted(set(income_data.keys()) | set(expense_data.keys()))

    print("Income vs Expenses (Monthly):")
    for month in all_months:
        income = income_data.get(month, 0)
        expense = expense_data.get(month, 0)
        balance = income - expense
        print(f"- {month}: Income ₹{income:.2f} | Expenses ₹{expense:.2f} | Balance ₹{balance:.2f}")

def show_most_spent_items():
    monthly_spending = defaultdict(lambda: defaultdict(float))
    yearly_spending = defaultdict(lambda: defaultdict(float))

    if not os.path.exists(EXPENSE_FILE):
        print("No expenses found.")
        return

    with open(EXPENSE_FILE, "r") as file:
        for line in file:
            try:
                date_str, amount, item, _ = line.strip().split(",")
                date = datetime.strptime(date_str, "%Y-%m-%d")
                month = date.strftime("%Y-%m")
                year = date.strftime("%Y")
                monthly_spending[month][item] += float(amount)
                yearly_spending[year][item] += float(amount)
            except ValueError:
                continue

    print("Most Spent Items per Month:")
    for month in sorted(monthly_spending):
        item, amount = max(monthly_spending[month].items(), key=lambda x: x[1])
        print(f"- {month}: ₹{amount:.2f} on {item}")

    print("Most Spent Items per Year:")
    for year in sorted(yearly_spending):
        item, amount = max(yearly_spending[year].items(), key=lambda x: x[1])
        print(f"- {year}: ₹{amount:.2f} on {item}")

def main():
    while True:
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Add Income")
        print("4. View Income")
        print("5. Monthly & Yearly Average Expenses")
        print("6. Monthly Average Income")
        print("7. Income vs Expense Comparison")
        print("8. Most Spent Item per Month & Year")
        print("9. Exit")

        choice = input("Enter choice (1–9): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            add_income()
        elif choice == "4":
            view_income()
        elif choice == "5":
            show_avg_expenses()
        elif choice == "6":
            show_avg_income()
        elif choice == "7":
            compare_income_vs_expenses()
        elif choice == "8":
            show_most_spent_items()
        elif choice == "9":
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()




