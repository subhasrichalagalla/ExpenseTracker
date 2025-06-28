=========================================
      Expense Tracker Project
=========================================

🔹 Project Overview:
A command-line based Python application that allows users to track daily income and expenses, view reports, and manage personal finances.

🔹 Folder Contents:

1. finance_tracker.py     - Main Python script to run the tracker
2. expenses.txt           - Automatically generated file to store expense records
3. income.txt             - Automatically generated file to store income records
4. README.md              - Project overview and usage guide (Markdown format)
5. index.txt              - This index file (explains folder structure)

🔹 Main Features:
- Add/view income (source, amount, date)
- Add/view expenses (category, item, date, and place)
- Get monthly/yearly average daily spending
- View monthly average income
- Compare income and expenses with balance
- Most spent item by month/year

🔹 Technologies Used:
- Python 3.x
- Built-in modules only (no external dependencies)

🔹 How to Run:
1. Open terminal in the project folder
2. Run the script:
   python finance_tracker.py

🔹 Author:
[Chalagalla Sai Subha Sri]

Sample Output:
1)Enter income date (YYYY-MM-DD): 2025-06-01
Enter income amount (in ₹): 25000
Enter income source (e.g., Salary, Freelance): Salary
₹25000.00 added from 'Salary' on 2025-06-01.
2)Enter expense date (YYYY-MM-DD): 2025-06-02
Enter expense amount (in ₹): 100
Enter expense category (e.g., Food, Travel, Shopping, Rent, Entertainment, Health, Education, Bills): Travel
From where (e.g., Home): Home
To where (e.g., College): College
₹100.00 expense added for 'Travel from Home to College' under 'Travel' category.
3)Enter expense date (YYYY-MM-DD): 2025-06-03
Enter expense amount (in ₹): 300
Enter expense category (e.g., Food, Travel, Shopping, Rent, Entertainment, Health, Education, Bills): Food
Enter item (e.g., Momos, T-Shirt): Momos
Enter shop/place (e.g., GVK Mall): Food Court
₹300.00 expense added for 'Momos at Food Court' under 'Food' category.
4)Date        | Amount | Item                          | Category
2025-06-02  | ₹100   | Travel from Home to College   | Travel
2025-06-03  | ₹300   | Momos at Food Court           | Food
5)Monthly Average Daily Spending:
- 2025-06: ₹200.00 per day (₹400.00 over 2 day(s))

Yearly Average Daily Spending:
- 2025: ₹200.00 per day (₹400.00 over 2 day(s))
6)Average Monthly Income:
- 2025-06: ₹25000.00
Average: ₹25000.00 over 1 month(s)
7)Most Spent Items per Month:
- 2025-06: ₹300.00 on Momos at Food Court

Most Spent Items per Year:
- 2025: ₹300.00 on Momos at Food Court
=========================================

