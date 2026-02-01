#expense traker project code
expenseslist=[] #list of expenses[dictinory]

print('welcome to "Expense Tracker🙂"')
while True:
    print("===MENU===")
    print("1. Add Expenses")
    print("2. View All Expenses")
    print("3. View Total Expenses")
    print("4. exit")

    choice= int(input("Please enter your choice: ",))
    
    #add expance
    if(choice==1):                                      
        date= input("enter the date: ",)
        catagory=input("type of catagory(food , stationery): ",)
        description=input("enter detail: ",)
        amount=float(input("enter the amount: ",))
    #dictionary
        expense={"date": date,                              
                 "catagory": catagory,
                 "description": description,
                 "amount":amount
        }
        expenseslist.append(expense)
        print("\n expenses added succesfully")

    #view
    elif(choice==2):
        if(len(expenseslist)==0):
            print("no expenses added")
        else:
            print("==THIS IS YOUR EXPENSES==")
            count=1
            for each in expenseslist:
                print(f"Sr.no {count}-> {each["date"]}, {each["catagory"]}, {each["description"]}, {each["amount"]},")
                count+=1
    #total
    elif(choice==3):
        total=0
        for each in expenseslist:
            total=total+each["amount"]
        print("\nTOTAL =",total)

    #exit
    elif(choice==4):
        print("THANKYOU FOR USING OUR SYSTEM")
        break
    #error
    else:
        print("error and try again")

