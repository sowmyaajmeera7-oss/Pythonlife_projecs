dictionary = {}
while True:
     print("\n---- dictionary word----")
     print("1, add a word")
     print("2, search for meaning")
     print("3, display all word")
     print("4, update meaning")
     print("5, delate word")
     print("6, exit")

     print("code is successfully")
     choice = input("enter your choice (1-6):")

# add a word:
     if choice == '1':
      word = input("enter the word").lower()


      meaning = input("enter the meaning")
      word = [word] = meaning
      print("code is successfully!")

  # search for meaning:    
     elif choice == '2':
        word = input('enter the meaning:')

        if choice :
           print("/... the word is a meanig")
           print("the search for meaning ")
        else:
           print("code is successfully:")

    # display all word:
     elif choice == '3':
        word = input("enter the display:")

        if choice:
           print("display meanig")
        else:
           print("code is successfully")

# update meaning:
     elif choice == '4':
        word = input("enter the meaning:")
        if choice:
           print("the update ")
        else:
           print("code is successfully:")

# delate word:
     elif choice == '5':
        word= input("enter the delate word:")

        if choice:
           print("thr delate is a word")
        else:
           print("code is successfully")
     
# exit:
     elif choice == '6':
        word = input("enter the exit:")
        print("thank you code is end")
        break
#envalid
else:
    print("thank you code end")


    
     



