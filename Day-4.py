#BEGINNER
day=int(input("Enter number of days:"))
expenses=[]
for i in range(1,day+1):
     amount=float(input(f"Enter expenses of day{i}:"))
     expenses.append(amount)
     total=sum(expenses)
     avg=total/day
print("Total Expense:",total)
print("Average Expense:",avg)

#INTERMEDIATE
expense=int(input("Enter number of expense:"))
exp_amt=[]
category_total={}
for i in range(1,expense+1):
    amount=float(input(f"Expense {i} amount:"))
    category=input(f"expense {i} category:")
    exp_amt.append(amount)
    if amount>500:
      print("High expense detected")
    if category in category_total:
     category_total[category]+=amount
    else:
     category_total[category]=amount
total=sum(exp_amt)
avg=total/expense
highest=max(category_total,key=category_total.get)
if avg<=200:
    spending_status="Controlled Spending"
elif avg<=400:
    spending_status="Moderate Spending"
else:
    spending_status="High Spending"

print("-----Expense Summary-----")
print("Total Expense:",total)
print("Average Expense:",avg)
print("\n Category wise expense:")
for category, amount in category_total.items():
    print(f"{category}:{amount}")
print("Highest Spending Category:",highest)
print("Spending Status:",spending_status)


