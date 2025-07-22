# Complete this ATM simulation
balance = 1000
pin = "1234"

entered_pin = input("Enter PIN: ")
if entered_pin == pin:
    print("PIN accepted")
    while True:
        print("\n1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit") 
        print("4. Exit")
        
        choice = input("Choose option: ")
        
        # Complete the menu logic here
        # Your code here:
        if choice == "4":
            break
        if choice == "3":
            faktang = float(input("deposit amount:" ))
            if faktang < 0:
                print("cannot deposit less than 0")
                continue
            else:
             balance = balance + faktang
            print("success , your balance now =", balance)

        if choice == "2":
            tontang = float(input("withdawn amount:"))
            if tontang <= balance: 
             balance -= tontang
             print("success , your balance now=", balance)
             continue
            else :
             print("cannot withdawn less than 0 or more than balance")
            

        if choice == "1":
            print("your balance now =" ,balance)
        
        else:
            continue
 
else:
    print("Invalid PIN")