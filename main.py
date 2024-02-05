import utilities
import db
import order
import bill



while True:
    print("              WELCOME TO LOGIN PAGE             ")
    print("                     MENU                       ")
    print("________________________________________________")
    print("                                                ")
    print("|   PRESS 1 TO REGISTER                        |")
    print("|   PRESS 2 TO LOGIN                           |")
    print("|   PRESS 3 TO EXIT                            |")
    ch = int(input("Please enter your choice: "))
    if ch == 1:
        username=input("Enter username: ")
        password=input("Enter your password: ")
        mobile=int(input("Enter your mobile no.: "))
        address=input("Enter you address: ")

        print("Registration sucessfull")
        conn = db.create_connection()    
        registration_status = db.insert_data(username,password,mobile,address)
        db.close_connection(conn)
        continue

    elif ch == 2:
        username=input("Enter your username: ")
        passwd=input("Enter your password: ")
        
        conn = db.create_connection()
        login_status = utilities.login(username,passwd)
        db.close_connection(conn)

        if login_status == 1:
            print('login sucessfull')
        elif login_status==0:
            reset_choice = input("Wrong Pssword! Do you want to reset your password? Enter YES to reset: ").upper()
            if reset_choice == 'YES':
                reset=utilities.forget(username, passwd)
                if reset==1:
                    continue
                else:
                    continue
        elif login_status==-1:
            continue
    

    elif ch == 3:
        print("Thank you!")
        continue
    else:
        print("Please enter a valid choice")
        continue

    break
name=input("Please enter your name: ")
while True:
    print("---------Salt and Sizzle -----------")
    print("Hello",name,", What would you like to order?")


    print("|                   MENU                       |")
    print("|   PRESS 1. PIZZA                             |")
    print("|   PRESS 2. BURGER                            |")
    print("|   PRESS 3. SANDWICH                          |")
    print("|   PRESS 4. ROLL                              |")
    print("|   PRESS 5. BIRYANI                           |")
    print("|   PRESS 6. EXIT                              |")

    choice=int(input("Please enter your choice: "))
    print("                     ")
    if(choice==1):
        order.show_pizza_menu()
        a=input("Do you want to continue with menu? Enter YES to continue: ").upper() 
        if a== 'YES':
            continue
        else:
            break
        

    elif(choice==2):
        order.show_burger_menu()
        a=input("Do you want to continue with menu? Enter YES to continue: ").upper() 
        if a== 'YES':
            continue
        else:
            break

    elif(choice==3):
        order.show_sandwich_menu()
        a=input("Do you want to continue with menu? Enter YES to continue: ").upper() 
        if a== 'YES':
            continue
        else:
            break

    elif(choice==4):
        order.show_roll_menu()
        a=input("Do you want to continue with menu? Enter YES to continue: ").upper() 
        if a== 'YES':
            continue
        else:
            break

    elif(choice==5):
        order.show_biryani_menu()
        a=input("Do you want to continue with menu? Enter YES to continue: ").upper() 
        if a== 'YES':
            continue
        else:
            break
    
    elif(choice==6):
        print("Thank you!")
        a=input("Do you want to continue with menu? Enter YES to continue: ").upper() 
        if a== 'YES':
            continue
        else:
            break

    else:
        print("Print a valid choice")

    break


bill=bill.generate_bill()
print("                     ")
print("Your total bill is: ",bill)
print("                    ")
print("Thank you for visiting Salt and Sizzle.")
print("Visit again")
print("Have a nice day!")



