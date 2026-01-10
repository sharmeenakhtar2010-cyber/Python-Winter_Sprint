Credential_list=[]
print("WELCOME TO CREDENTIAL MANAGER")
while True:
    print("-----Vault lite-----")
    print("1. Add credentials")
    print("2. View credentials")
    print("3. Update credentials")
    print("4. Exit")
    choice=int(input("choose a number:"))
    if choice==1:
       print("Add your credentials")
       website=input("enter website:")
       
       username=input("enter username")
       password=(input("enter password"))
       credential= {"website":website, "username":username, "password":password}
       Credential_list.append(credential)
       print("CREDENTIAL SAVED SUCCESSFULLY")
    elif choice==2:
        print("SAVED CREDENTIAL")
        count=1
        for eachcredential in Credential_list:
            print(f"{count}.{eachcredential['username'] } @ {eachcredential['website']} ")
            count+=1
    elif choice==3:
        if (len(Credential_list)==0):
            print("NO CREDENTIAL TO UPDATE")
        else:
            print("UPDATED CREDENTIALS")
            count=1
            for eachcredential in Credential_list:
               print(f"{count}.{eachcredential['username']} @ {eachcredential['website']}")
               count+=1
            update_choice=int(input("enter number of choice:"))
            if 1<= update_choice <= len(Credential_list):
              new_password=input("enter new password:")

              Credential_list[update_choice-1]["password"]=new_password
              print("PASSWORD UPDATED SUCCESSFULLY")
            else:
             print("INVALID NUMBER")
    elif choice==4:
       print("THANK YOU FOR USING OUR SYSTEM")
       break
    else:
       print("INVALID CHOICE")
