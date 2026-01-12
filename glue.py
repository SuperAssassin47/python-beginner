def june_2019():
    pizzaPrices = {"small": 3.25, "medium": 5.50, "large": 7.15}
    toppingPrices = {0: 0, 1: 0.75, 2: 1.35, 3: 2.00, 4: 2.50}

    deliveryCharge = 2.50

    pizza_sizes = ["small", "medium", "large"]

    while True:
        customerName = input("Enter customer name: ")

        if customerName.isalpha():
            print("[/] SUCCESS!! Data is valid. Thanks :)")
            break
        else:
            print("[X] ERROR!! Name isn't alphabetic. Try again :(")

    while True:
        customer_addr = input("Enter customer address: ")

        if customer_addr.strip():
            print("[/] SUCCESS!! Data is valid. Thanks :)")
            break
        else:
            print("[X] ERROR!! Address isn't alphanumeric. Try again :(")

    while True:
        contactInfo = input("Enter contact info: ")

        if contactInfo.isdigit():
            print("[/] SUCCESS!! Data is valid. Thanks :)")
            break
        else:
            print("[X] ERROR!! Contact Info is not an integer. Try again :(")

    while True:
        numPizzas = int(input("\nHow many pizzas would you like to order?: "))

        if 1 <= numPizzas <= 6:
            print("[/] SUCCESS!! Data is valid. Thanks :)")
            break
        else:
            print("[X] ERROR!! Pizza Quantity is outside of scope. Try again :(")

    while True:
        pizzaSize = input("How big would you like the pizza to be?: ")

        if pizzaSize in pizza_sizes:
            print("[/] SUCCESS!! Data is valid. Thanks :)")
            break
        else:
            print("[X] ERROR!! Unknown data. Try again :(")

    while True:
        try:
            extraToppings = int(input("How many toppings would you like?: "))

            if 1 <= extraToppings <= 4:
                print("[/] SUCCESS!! Data is valid. Thanks :)")
                break
            else:
                print("[X] ERROR!! Pizza toppings quantity is invalid. Try again :(")
        except ValueError:
            print("[X][X] CATASTROPHIC ERROR!! Input must be an integer. Try again :(")

    deliveryRequest = input("Would you like us to deliver your order directly to you? (y/n): ")

    pizzaCost = pizzaPrices[pizzaSize] * numPizzas
    toppingCost = toppingPrices[extraToppings]
    standardCost = pizzaCost + toppingCost

    if (deliveryRequest == "y" or deliveryRequest == "Y") and standardCost > 20:
        discountCost = standardCost * 0.9
        finalCost = discountCost + deliveryCharge
        print(f"\n|| =====PERSONALISED AND ITEMISED BILL===== ||")
        print(f"|| Customer Name: {customerName}           ||")
        print(f"|| Customer Address: {customer_addr}       ||")
        print(f"|| Customer Contact Info: {contactInfo}    ||")
        print("\n")
        print(f"|| Pizzas ordered: {numPizzas}             ||")
        print(f"|| Size of Pizzas: {pizzaSize}             ||")
        print(f"|| Extra Toppings: {extraToppings}         ||")
        print("\n")
        print(f"The total cost for your order is {finalCost:.2f},"
              f"includes the pizza size, quantity of pizzas,"
              f"any extra toppings and a 10% discount.")
        print(f"\n")
        print(f"You have requested for a delivery of your order."
              f"The charge for the delivery will be accrued at: {deliveryCharge}"
              f"\nEnjoy!!")


    elif (deliveryRequest == "n" or deliveryRequest == "N") and standardCost > 20:
        # noinspection PyTypeChecker
        discountCost = standardCost * 0.9
        finalCost = discountCost
        print(f"\n|| =====PERSONALISED AND ITEMISED BILL===== ||")
        print(f"|| Customer Name: {customerName}           ||")
        print(f"|| Customer Address: {customer_addr}       ||")
        print(f"|| Customer Contact Info: {contactInfo}    ||")
        print("\n")
        print(f"|| Pizzas ordered: {numPizzas}             ||")
        print(f"|| Size of Pizzas: {pizzaSize}             ||")
        print(f"|| Extra Toppings: {extraToppings}         ||")
        print("\n")
        print(f"The total cost for your order is {finalCost:.2f},"
              f"includes the pizza size, quantity of pizzas,"
              f"any extra toppings and a 10% discount."
              f"\nEnjoy!!")

    else:
        finalCost = standardCost
        print(f"\n|| =====PERSONALISED AND ITEMISED BILL===== ||")
        print(f"|| Customer Name: {customerName}           ||")
        print(f"|| Customer Address: {customer_addr}       ||")
        print(f"|| Customer Contact Info: {contactInfo}    ||")
        print("\n")
        print(f"|| Pizzas ordered: {numPizzas}             ||")
        print(f"|| Size of Pizzas: {pizzaSize}             ||")
        print(f"|| Extra Toppings: {extraToppings}         ||")
        print("\n")
        print(f"The total cost for your order is {finalCost:.2f},"
              f"includes the pizza size, quantity of pizzas,"
              f"any extra toppings."
              f"\nEnjoy!!")

def LawnCareCostCalculator():
    # Lawn Care products costs
    luxury = 1.15  # excluding VAT
    standard = 0.80  # excluding VAT
    economy = 0.45  # excluding VAT

    # lawn care products
    lawncareProducts = ["Luxury", "Standard", "Economy"]

    # collecting customer information
    customerName = input("Enter customer name: ")
    customerAddress = input("Enter customer address: ")
    customerContactInfo = input("Enter contact info: ")

    # validating the lawn width
    while True:
        lawnWidth = int(input("Enter width of lawn: "))  # collecting the info

        if 2 <= lawnWidth <= 30:  # parsing it to this, to test against this criteria
            print("[/] SUCCESS!! Data is valid. Thanks :)")  # if the test passed, output this message
            break  # escape the loop
        else:  # if test failed, output the error message and re-prompt
            print("[X] ERROR!! Input out of scope. Try again :(")

    # validating the lawn length
    while True:
        lawnLength = int(input("Enter length of lawn: "))  # collecting the info

        if 2 <= lawnLength <= 50:  # parsing it to this, to test against this criteria
            print("[/] SUCCESS!! Data is valid. Thanks :)")  # if test passed, output this message
            break  # escape the loop
        else:  # if test failed, output this error mesage and re-prompt
            print("[X] ERROR!! Input out of scope. Try again :(")

    # calculating the area of the lawn
    metresSquared = lawnLength * lawnWidth

    # asking the user which lawn care product they would like from the given selection: Luxury, Standard or Economy
    lawnCare = input("Which quality of lawn care products would you like?: ")

    # if the user selected Luxury
    if lawnCare == lawncareProducts[0]:

        # calculate the total cost
        totalCost = metresSquared * 0.50 * luxury

        # display the itemised bill along with the total cost opf labour
        print("|| ----- PERSONALISED AND ITEMISED BILL ----- ||")
        print(f"|| Customer Name: {customerName}")
        print(f"|| Customer Address: {customerAddress}")
        print(f"|| Contact Information: {customerContactInfo}")
        print("\n")
        print("|| ----- DESCRIPTION OF COSTINGS ----- ||")
        print(f"|| Width of Lawn: {lawnWidth}")
        print(f"|| Length of lawn: {lawnLength}")
        print(f"|| Quality of lawn care products selected: {lawnCare}")
        print("\n")
        print(f"|| Total cost of labour: £{totalCost:.2f}")

        # ask the user if they would like to add VAT on top of their total cost
        vat = input("Would you like to add VAT onto your total cost? (y/n): ")
        if vat == "y" or vat == "Y":  # if yes, calculate the final cost and add them together
            finalCost = totalCost * 0.2

            finalAccrue = finalCost + totalCost

            print(f"|| Your final cost is: £{finalAccrue:.2f}")  # displaying the final accrued costings

    # if the user selected Standard
    elif lawnCare == lawncareProducts[1]:

        # calculate the total cost
        totalCost = metresSquared * 0.50 * standard

        # display the itemised bill along with the total cost
        print("|| ----- PERSONALISED AND ITEMISED BILL ----- ||")
        print(f"|| Customer Name: {customerName}")
        print(f"|| Customer Address: {customerAddress}")
        print(f"|| Contact Information: {customerContactInfo}")
        print("\n")
        print("|| ----- DESCRIPTION OF COSTINGS ----- ||")
        print(f"|| Width of Lawn: {lawnWidth}")
        print(f"|| Length of lawn: {lawnLength}")
        print(f"|| Quality of lawn care products selected: {lawnCare}")
        print("\n")
        print(f"|| Total cost of labour: £{totalCost:.2f}")

        # ask the user if they would like to add VAT on top of the total cost
        vat = input("Would you like to add VAT onto your total cost? (y/n): ")
        if vat == "y" or vat == "Y":  # if yes, calculate the final cost and them together
            finalCost = totalCost * 0.2

            finalAccrue = finalCost + totalCost

            print(f"|| Your final cost is: £{finalAccrue:.2f}")  # display the final accrued costings
    else:  # if user selected economy

        # calculate the total cost
        totalCost = metresSquared * 0.50 * economy

        # display the itemised bill along with the total cost
        print("|| ----- PERSONALISED AND ITEMISED BILL ----- ||")
        print(f"|| Customer Name: {customerName}")
        print(f"|| Customer Address: {customerAddress}")
        print(f"|| Contact Information: {customerContactInfo}")
        print("\n")
        print("|| ----- DESCRIPTION OF COSTINGS ----- ||")
        print(f"|| Width of Lawn: {lawnWidth}")
        print(f"|| Length of lawn: {lawnLength}")
        print(f"|| Quality of lawn care products selected: {lawnCare}")
        print("\n")
        print(f"|| Total cost of labour: £{totalCost:.2f}")

        # ask user if they would like to add VAT on top of the total cost
        vat = input("Would you like to add VAT onto your total cost? (y/n): ")
        if vat == "y" or vat == "Y":  # if yes, calculate the final cost and add them together
            finalCost = totalCost * 0.2

            finalAccrue = finalCost + totalCost

            print(f"|| Your final cost is: £{finalAccrue:.2f}")  # display the final accrued costings

def passwordChecker():
    # loop that continues to run until the user enters a password
    while True:
        # asking the user to enter their password to be rated
        userPassword = input("Enter password to be rated: ")  # saving it to a variable for later use
        if userPassword == "  ":
            print("[X] ERROR!! No password has been entered. :(")
        else:
            print("[/] SUCCESS!! Password has been entered. :)")
            break
    # defining constants
    lowerCase = 0  # count how many lowercase letters there are in the password
    upperCase = 0  # count how many uppercase letters there are in the password
    digits = 0  # count how many integers there are in the password
    specialChars = 0  # count how many special characters there are in the password
    # iterating through the stored password inside the 'userPassword' variable
    for char in userPassword:
        if char.islower():  # checks if there are lowercase letters
            lowerCase += 1  # increments the count by one if a lowercase letter is found
        elif char.isupper():  # checks if there are upper case letters
            upperCase += 1  # increments the count by one if an uppercase letter is found
        elif char.isdigit():  # checks if there are digits
            digits += 1  # increments the count by one if a digit is found
        else:
            specialChars += 1  # increments the count by one if a special character is found
    # performing the calculation by multiplying the totals of each of the previously modified constants by the point rate
    # lowercase: 5 per letter
    # uppercase: 5 per letter
    # digits: 10 per digit
    # special character: 10 per special character
    points = (lowerCase * 5) + (upperCase * 5) + (digits * 10) + (specialChars * 10)
    # 20 is added to the total points IF the password contains 10 or more digits
    if userPassword >= "10":
        points = points + 20
    # IF the password is all lower case, deduct 3 points from the total score
    if userPassword.islower():
        print("Weak Password!! Only lowercase letters have been detected. :(")
        points = points - 3
    # IF the password is all upper case, deduct 3 points from the total score
    if userPassword.isupper():
        print("Weak Password!! Only uppercase letters have been detected. :(")
        points = points - 3
    # IF the password is all integers, deduct 5 points from the total score
    if userPassword.isdigit():
        print("Weak Password!! Only integers have been detected. :(")
        points = points - 5
    # output the final password rating report with string concatenation
    print("\n----|| PASSWORD RATING REPORT ||----")
    print(f"LowerCase Letters used: {lowerCase}")
    print(f"UpperCase Letters used: {upperCase}")
    print(f"Integers used: {digits}")
    print(f"Special Characters used: {specialChars}")
    print(f"Total Password Score: {points}")
    # IF password score is less than 20, password security rating is Very Low
    if points <= 20:
        print("Security Rating: Very Low :(")
    # IF password score is between 21 and 40, password security rating is Low
    elif points >= 21 and points <= 40:
        print("Security Rating: Low :(")
    # IF password score is between 41 and 70, password security rating is Medium
    elif points >= 41 and points <= 70:
        print("Security Rating: Medium :|")
    # IF password score is between 71 and 80, password security rating is High
    elif points >= 71 and points <= 80:
        print("Security Rating: High :)")
    # otherwise, password security rating is Very High
    else:
        print("Security Rating: Very High :)")

def currencyConversionCalculator():
    # declaring constants to permanently store the exchange
    # rates for each of the five currencies.
    US_Exchange_Rate = 1.40
    EU_Exchange_Rate = 1.14
    BRL_Exchange_Rate = 4.77
    JPY_Exchange_Rate = 151.05
    TRY_Exchange_Rate = 5.68

    # defining variables and assigning the default value "0".
    transactionFee = 0
    convertedAmount = 0

    # initialising a list with the five currency codes.
    currencies = ["USD", "EUR", "BRL", "JPY", "TRY"]

    # while loop to validate the value of GBP_amount
    while True:
        # collecting GBP information as a floating point number and assigning it to a variable
        GBP_amount = float(input("Enter GBP amount is: "))
        # checks if the GBP amount is between £1 and £2500
        if 1.00 <= GBP_amount <= 2500.00:
            print("[/] SUCCESS!! Data is valid. Thanks :)")
            # terminate the loop here
            break
        else:
            # display and re-prompt
            print("[X] ERROR!! Data not valid. Please try again :(")

    # collecting the choice of currency to convert to and assigning it to a variable
    customerCurrency = input("Which currency would you like to convert to?: ")

    # conditional statement to test the user input to see if it matches the specified criteria.
    if customerCurrency == currencies[0]:
        convertedAmount = GBP_amount * US_Exchange_Rate
        transactionFee = convertedAmount * 0.035
    elif customerCurrency == currencies[1]:
        convertedAmount = GBP_amount * EU_Exchange_Rate
        transactionFee = convertedAmount * 0.03
    elif customerCurrency == currencies[2]:
        convertedAmount = GBP_amount * BRL_Exchange_Rate
        transactionFee = convertedAmount * 0.025
    elif customerCurrency == currencies[3]:
        convertedAmount = GBP_amount * JPY_Exchange_Rate
        transactionFee = convertedAmount * 0.02
    elif customerCurrency == currencies[4]:
        convertedAmount = GBP_amount * TRY_Exchange_Rate
        transactionFee = convertedAmount * 0.015
    # only runs if all other branches return false
    else:
        print("[X] ERROR!! Invalid currency choice. Please try again :(")

    # calculating the total cost and assigning to a variable
    totalCost = GBP_amount + transactionFee

    # while loop to validate the user input for the staff verification check
    while True:
        # asking the user if they are a member of staff
        staffConfirm = input("Are you a member of staff? (y/n): ")

        # checks if the value of staffConfirm is an alphabetic string
        if staffConfirm.isalpha():
            print("[/] SUCCESS!! Answer is valid. Thanks :)")
            # terminate the loop here
            break
        else:
            # display and re-prompt
            print("[X] ERROR!! Answer not valid. Please try again :(")

    # conditional statement to check if the customer is a member of staff and get a 5% staff discount.
    if staffConfirm == "y" or staffConfirm == "Y":
        firstPart = totalCost / 100 * 5
        staffDiscount = totalCost - firstPart
        print("\n============CURRENCY CONVERSION REPORT============")
        print(f"Your converted amount from GBP to {customerCurrency} is: ($/€/R$/¥/₺) {convertedAmount:.2f}."
              f"\nThe transaction fee for conversion is: £{transactionFee:.2f}."
              f"\n"
              f"The total cost for you to pay for the conversion is: £{totalCost:.2f},"
              f"\nincludes a staff discount of £{staffDiscount:.2f}."
              f"\nHave a nice day :)")
    # only runs if the if branch returns false
    elif staffConfirm == "n" or staffConfirm == "N":
        print("============CURRENCY CONVERSION REPORT============")
        print(f"Your converted amount from GBP to {customerCurrency} is: ($/€/R$/¥/₺) {convertedAmount:.2f}."
              f"\nThe transaction fee for the conversion is £{transactionFee:.2f}"
              f"\n"
              f"The total cost for you pay for the conversion is: £{totalCost:.2f}"
              f"\nHave a nice day :)")
