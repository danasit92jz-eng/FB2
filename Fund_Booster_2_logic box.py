# Logic Box
# Pattern Generator and Number Analyzer

print("_____LOGIC BOX_____")
print("Welcome to Pattern Generator and Number Analyzer!")

while(True):

    print("\n----------- MENU -----------")
    print("1.Generate Pattern")
    print("2.Analyze Numbers")
    print("3.Exit")
    choice = int(input("Enter your choice: "))
    #code for Pattern
    if choice == 1:
        rows = int(input("Enter number of rows: "))
        if rows <= 0:
            print("Invalid input..... rows enter by you is always possitive number")
            break
        print("\nPattern:")
        
        for i in range(rows):
            for j in range(i+1):
                print("*", end="")
            print()

    # Number Analyzer
    elif choice == 2:
        start = int(input("Enter start number: "))
        end = int(input("Enter end number: "))

        if end <= start:
            print("Invalid input for starting and ending rang!")
            print("End number must be greater than start number.")
            continue
        Add = 0

        print("\nNumber Analysis:")
        for i in range(start, end + 1):
            Add = Add + i

            # even odd or zero
            if i == 0:
                print("Number 0 is Zero")
                continue
            if i % 2 == 0:
                print("Number", i, "is Even")
            else:
                print("Number", i, "is Odd")
        print("\nSum of all numbers:", Add)

    # Exit
    elif choice == 3:
        print("\n**********Thank you**********")
        break
    # Invalid Choice
    else:
        print("Invalid choice!")
        pass
