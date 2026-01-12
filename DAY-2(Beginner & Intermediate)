 #BEGINNER LEVEL
Name=input("Enter your name:")
Age=int(input("Enter your age:"))
subject1=input("Enter subject1:")
subject2=input("Enter subject2:")
subject3=input("Enter subject3:")
Roll_number=int(input("Enter roll number:"))
Branch=input("Enter branch:")
Marks1=int(input("Enter marks of subject1:"))
Marks2=int(input("Enter marks of subject2:"))
Marks3=int(input("Enter marks of subject3:"))
Skill1=input("Enter skill 1:")
Skill2=input("Enter skill 2:")
Skill3=input("Enter skill 3:")

print("------STUDENT DETAILS-----")
print("Name:",Name)
print("Age:",Age)
Favourite_subjects=[subject1,subject2,subject3]
print("Favourite subject:",Favourite_subjects)
Student_Info=(Roll_number,Branch)
print("Student Info:",Student_Info)
Marks={subject1:Marks1, subject2:Marks2, subject3:Marks3}
print("Marks:",Marks)
Technical_Skills={Skill1,Skill2,Skill3}
print("Technical Skills:",Technical_Skills)

 #INTERMEDIATE LEVEL
name=input("Enter your full name:")
roll_number=int(input("Enter roll number:"))
branch=input("Enter branch:")
fav_sub=input("Enter your favourite subjects(comma separated):")
Fav_subject=fav_sub.split(",")
Fav_subject.sort()
marks={}
for subject in Fav_subject:
    subject=subject.strip()
    mark=int(input(f"Enter marks for {subject}"))
    marks[subject]=mark
total_marks=sum(marks.values())
average_marks=total_marks/len(marks)


tech_skills=input("Enter technical skills (comma saparated):")
Technical_skills=tech_skills.split(",")
max_marks=max(marks,key=marks.get)
print("-----STUDENT DETAILS-----")
print("Full name",name)
print("Roll Number & Branch:",roll_number,branch)
print("Favourite Subjects(Alphabetical):", Fav_subject)
print("Subject-wise marks:",marks)
print("Total Marks:",total_marks)
print("Average Marks:",average_marks)
print("Highest Scoring Subject:",max_marks)
print("Technical skills:",Technical_skills)
