Atm = input("enter the atm card:,")
Acount =input("enter the account numbers:,")
Amount = input("enter the amount:,")


Balance = 0
while True:
    print("\nATM menu")
    print(1,"creadit")
    print(2,"deposite")
    print(3,"balance")
    print(4,"exit")
# CREADIT:
    choice = input("ente the choice(1-6):,")
    if choice == '1':
        amount = float(input("enter the amount to creadit:"))
        if amount <=2:
            print("plesa enter a positive amount,")
        else:
            Balance += amount
            print(f"${amount} creadit to you account.")
# DEPOSITE:
    elif choice == '2':
        amount = float(input('enter amount to deposite:'))
        if amount <=0:
            print("please enter a positive amount.")
        elif amount > Balance:
            print("insufficent balance.")
        else:
            Balance -= amount
            print(f"${amount}deposite fromyour account.")

  # BALANCE:          
    elif choice == '3':
        print(f"your currect balance is: ${Balance}")

    elif choice == '4':
        print("thank you for using tha ATM. goodby!")
        break
    else:
        print("invalid choice. please try again.")

# EXIT:
else:
    print("the amount is successfully.")


 