def find_number():
    # Ask the user for input N (positive integer) 
    n = int(input("Please input a positive integer: "))
    print(f"N = {n}")
    numbers = []

    # Ask the user to provide N numbers one by one and read all of them one by one
    print(f"\nPlease input {n} numbers one by one.")
    for i in range(n):
        num = int(input(f"Enter number {i + 1}: "))
        numbers.append(num)

    # Ask for the number X to find
    x = int(input("\nEnter the number to find: "))

    # Find the index of X in the list of numbers
    print(f"\nThe index of {x} is:")
    if x in numbers:
        print(f"{numbers.index(x) + 1}")
    else:
        print("-1")


find_number()
