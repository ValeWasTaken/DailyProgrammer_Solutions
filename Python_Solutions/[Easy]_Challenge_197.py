import random

def main():
    choice = raw_input("\n1.) Check ISBN validity. \n2.) Generate ISBN \n3.) Exit\n\n")
    if choice == "1":
        ISBN_Check(raw_input("Enter ISBN: "))
    elif choice == "2":
        gen_ISBN()
    elif choice == "3":
        exit()
    else:
        print("Error. Please try again. \n\n")
        main()
    main()

def ISBN_Check(data):
    ISBN = 0
    x = 10
    
    for number in range(len(data)):
        ISBN += (int(data[number])*x)
        x -= 1

    if ISBN % 11 == 0:
        #print("Valid ISBN!")
        return(True)
    else:
        #print("Invalid ISBN.")
        return(False)

def gen_ISBN():
    ISBN = str(random.randint(1000000000, 9999999999))
    while ISBN_Check(ISBN) != True:
            ISBN = str(random.randint(1000000000, 9999999999))
            ISBN_Check(ISBN)
    print("\nYour valid ISBN is: "+str(ISBN))
main()
