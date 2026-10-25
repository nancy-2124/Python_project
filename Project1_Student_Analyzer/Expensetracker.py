expenses=[]
total=0
for i in range(3):
    amount=int(input("enter amount:"))
    category=input("enter category:")
    expense={"amount":amount, "category":category}
    expenses.append(expense)
for i, expense in enumerate(expenses, start=1):
    total=total+expense["amount"]
    print("Expense", i, ":", expense["amount"], "-", expense["category"])
print(total)