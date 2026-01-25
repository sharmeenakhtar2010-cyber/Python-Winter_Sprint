#FOUNDATION TRACK
name=input("Enter student name: ")
n=int(input("Enter number of subjects: "))
marks=[]
for i in range(1,n+1):
    sub=int(input(f"Enter marks for subjects {i}: "))
    marks.append(sub)
total=sum(marks)
avg=total/n
print("----- RESULT SUMMARY -----")
print("Student Name:",name)
print("Total Marks : ",total)
print("Average Marks: ",avg)
