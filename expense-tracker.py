#PERSONAL_EXPENSE_TRACKER
import csv
from datetime import datetime
import os
File_name='Expense.csv'
def add_transaction(amount,category,type):
  date=datetime.now().strftime("%Y-%m-%d")
  with open(File_name,mode='a',newline='') as file:
    writer=csv.writer(file)
    writer.writerow([date,amount,category,type])
  print("Transaction added successfully!!")
def show_summary():
  t_income=0
  t_expense=0
  try:
    with open(File_name,mode='r') as file:
      reader=csv.reader(file)
      for row in reader:
        date,amount,category,type=row
        amount=float(amount)
        if type.lower()=="income":
          t_income+=amount
        else:
          t_expense+=amount
      print("-SUmmary-")
      print("Total Income:",t_income)
      print("Total Expense:",t_expense)
      print("Balance:",t_income-t_expense)
  except FileNotFoundError:
        print("No transactions found.")
def show_transaction():
    try:
      with open(File_name,mode='r') as file:
        reader=csv.reader(file)
        print("-ALl transactions-")
        print(f"{'Date':<15}{'Amount':<12}{'Category':<15}{'Type':<10}")
        print("-"*10)
        for row in reader:
          date,amount,category,type=row
          print(f"{date:<15}{amount:<12}{category:<15}{type:<10}")
    except FileNotFoundError:
      print("No transactions found.")
def clear_data():
    with open(File_name,mode='w') as file:
      file.truncate(0)
    print("All Transaction data cleared sucessfully!!")
while True:
    print("\nPersonal Expense Tracker")
    print("1.Add Transaction")
    print("2.Show Summary")
    print("3.Show Transactions")
    print("4.Clear Data")
    print("5.Exit")
    choice=input("Enter your choice:")
    if choice=="1":
      amount=float(input("Enter amount:"))
      category = input("Enter category: ").strip()
      type= input("Income or Expense: ").strip().lower()
      add_transaction(amount,category,type.capitalize())
    elif choice=="2":
      show_summary()
    elif choice=="3":
      show_transaction()
    elif choice=="4":
      clear_data()
    elif choice=="5":
      print("Exiting the program.")
      break
    else:
      print("Invalid choice.Please try again.")
