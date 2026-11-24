todolist = {}
while True:
     print("\n---- to do list----")
     print("1, add a task")
     print("2, remove task")
     print("3, mark completed")
     print("4, display task")
     print('5. clear task')
     print("6, exit")
     choice = input("enter your choice (1-6):")


     if choice == '1':
      name = input("enter the task:").lower()
      print("task is successfully!")

     elif choice == '2':
        name = input('enter the remove task:')
        if choice :
           print("the task is a addedd")

        else:
           print("remove  is successfully:")

     elif choice == '3':
        name = input("enter the mark complate task:")

        if choice:
           print("list is complete")
        else:
           print("mark is successfully")


     elif choice == '4':
        name = input("enter the display task:")
        if choice:
           print("display task completed! ")
        else:
           print("display is successfully:")

     elif choice == '5':
        word= input("enter the clear task:")

        if choice:
           print("clear task completed")
        else:
           print("clear is successfully")
     
     elif choice == '6':
        name = input("enter the exit:")
        print("thank you list is sucessfully!..")
        break

else:
    print(" code is sucessfully!..")

