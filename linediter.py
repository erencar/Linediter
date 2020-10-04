from delsame import delsame
from differentlines import dif
from samelines import same

print("-------------------- !!! Welcome The LineEditer !!! ----------------------\n")

while True:

    print("Find the Similar Lines Between the 2 Text Files   : 1 \n")
    print("Find the Different Lines Between the 2 Text Files : 2 \n")
    print("Find the Similar Lines in the File and Delete     : 3 \n")
    print("EXIT : 0 \n")

    choice=int(input("What's Your Choice : "))

    if choice == 1:
        first = raw_input("Please Enter the 1. Text File Name = ")
        print("\n")
        second= raw_input("Please Enter the 2. Text File Name = ")
        same(first,second)
        print("\n")
        print("----------------------- !!! Please Check 'same-lines.txt' !!! ----------------------------------- \n")

    elif choice == 2:
        first = raw_input("Please Enter the 1. Text File Name = ")
        print("\n")
        second = raw_input("Please Enter the 2. Text File Name = ")
        dif(first, second)
        print("\n")
        print("----------------------- !!! Please Check the 'different-lines.txt' !!! -------------------------- \n")

    elif choice == 3:
        text = raw_input("Please Enter the Text File Name = ")
        delsame(text)
        print("\n")
        print("---------------------- !!! Please Check 'del-same.txt' !!! ------------------------------- \n")

    elif choice == 0:
        print("!!! Thank You !!!")
        break
