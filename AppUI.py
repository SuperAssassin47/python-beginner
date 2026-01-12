import sys
from glue import *


def show_menu():
    print("|| ===== PORTFOLIO APPLICATION ===== ||")
    print("|| =====   v1.0.0 Main Menu    ===== ||\n")

    print("Please select an option below to view:")
    print("1. Pizza Delivery Program")
    print("2. Lawn care Cost Calculator Program")
    print("3. Password Security Checker Program")
    print("4. Currency Conversion Calculator Program")
    print("5. Exit Portfolio Application")


while True:
    show_menu()
    data = int(input("> "))

    if data == 1:
        june_2019()
    elif data == 2:
        LawnCareCostCalculator()
    elif data == 3:
        passwordChecker()
    elif data == 4:
        currencyConversionCalculator()
    elif data == 5:
        confirm = input("Are you sure you want to quit the application? (y/n): ")

        if confirm == "y" or confirm == "Y":
            print("Exiting....")
            sys.exit()
    else:
        print("[X][X] CATASTROPHIC ERROR!! Please select a valid option from the menu above. Thanks")

    input("\nPress any key and hit [ENTER]....\n")
