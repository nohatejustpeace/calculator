print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divid")
print("5. Exit")
choice = input()
n1  = int(input("First Number: "))
n2 = int(input("Second Number: "))

if choice == "1":
    print(f"Answer is {n1 + n2}")
elif choice == "2":
    print(f"Answer is {n1 - n2}")
elif choice == "3":
    print(f"Answer is {n1 * n2}")
elif choice == "4":
    print(f"Answer is {n1 / n2}")
elif choice == "5":
    exit
else: 
    print("Invalid")