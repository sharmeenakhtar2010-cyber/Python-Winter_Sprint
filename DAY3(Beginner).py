#BEGINNER
name=input("Enter Username: ")
p1name=input("Enter product 1 name: ")
p1=int(input("Enter product 1 price: "))
p2name=input("Enter product 2 name: ")
p2=int(input("Enter product 2 price: "))
p3name=input("Enter product 3 name: ")
p3=int(input("Enter product 3 price: "))
print("-----CART SUMMARY-----")
print("User: ",name)
print("Products in Cart: ")
print(f"{p1name}:{p1}")
print(f"{p2name}:{p2}")
print(f"{p3name}:{p3}")
total=p1+p2+p3
dis=20
dis_amt=total*0.2
final=total-dis_amt
print("Total Amount: ",total)
print(f"Discount : {dis}%")
print("Final Amount: ",final)
