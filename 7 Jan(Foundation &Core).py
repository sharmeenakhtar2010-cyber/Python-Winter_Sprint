#Foundation
name=input("Enter patient name: ")
age=int(input("Enter age: "))
heart_rate=int(input("Enter heart rate: "))
city=input("Enter city: ")
name=name.title()
city=city.upper()
print(name)
print(city)
print("----------------------------------")
print("     CLINICAL DATA RECORD     ")
print("----------------------------------")
print("Patient Name: ",name)
print("Age: ",age)
print("Heart Rate:",heart_rate)
print("City:",city)
print("-------------------------------------")

#CORE
def validate_age(age,flags):
    if not age.isdigit():
        flags.append("Not an integer")
    age=int(age)
    if age<0 or age>120:
        flags.append("Invalid age")
       
def validate_heartrate(hr,flags,warnings):
    if not hr.isdigit():
       flags.append("Not an integer")
       return
    hr=int(hr)
    if hr>180:
        warnings.append("High heart rate detected")
       
def take_hr(n,flags,warnings):
    if n==0:
        return
    hr=input("enter heart rate reading: ")
    validate_heartrate(hr,flags,warnings)
    take_hr(n-1,flags,warnings)
def clinical_audit():
   flags=[]
   warnings=[]
   name=input("enter patient name:")
   age=input("enter age: ")
   validate_age(age,flags)
   readings=input("enter number of heart rate readings: ")
   if not readings.isdigit():
     flags.append("Invalid choice")
     readings=0
   else:
     readings=int(readings)
   take_hr(readings,flags,warnings)
   if flags:
      status="FAIL"
   elif warnings:
      status="REVIEW"
   else:
      status="PASS"

   print("--------CLINICAL AUDIT RESULT---------")
   print("Patient: ",name)
   print("Status: ",status)
   print("Flags: ",flags)
   print("Warnings",warnings)
clinical_audit()

       

                                                                                                                                                                         
