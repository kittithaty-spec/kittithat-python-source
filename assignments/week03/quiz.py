# Complete this program to classify people by age
age = int(input("Enter age: "))

# Add your if-elif-else statements here
# 0-12: Child
# 13-19: Teenager  
# 20-59: Adult
# 60+: Senior

# Your code here:
if age >= 90:
    print("very old")
elif age >= 80:
    print("old")
elif age >= 60:
    print("Almost old")
elif age >= 40:
    print("Working age")
elif age >= 20:
    print("Still Young")
elif age >= 10:
    print("Young")
else:
    print("Kid")
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
        if choice == "1":
            print(f"Your balance: {balance}")
        elif choice == "2":
            How_much = float(input("Enter amount: "))
            if How_much > balance:
                print("No try again")
            elif How_much <= balance:
                balance = balance - How_much
                print(f"balance now: {balance}")
        elif choice == "3":
            How_muchAdd = float(input("Enter amount: "))
            if How_muchAdd <= 0:
                print("No")
            elif How_muchAdd >0:        
             balance = balance + How_muchAdd
             print(f"balance now: {balance}")
        elif choice == "4":
            break            
else:
    print("Invalid PIN")
