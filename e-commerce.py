stock = {
    "iphone": 10,
    "samsung_phone": 5,
    "generic_phone": 7,
    "arcelik_tv": 3,
    "beko_tv": 4,
    "lg_tv": 6,
    "ipad": 8,
    "samsung_tablet": 10,
    "casper_tablet": 5,
    "apple_computer": 2,
    "casper_computer": 4,
    "monster_computer": 3,
    "airpods": 10,
    "mouse": 15
}

prices = {
    "iphone": 1000,
    "samsung_phone": 500,
    "generic_phone": 300,
    "arcelik_tv": 5000,
    "beko_tv": 2000,
    "lg_tv": 1500,
    "ipad": 1000,
    "samsung_tablet": 500,
    "casper_tablet": 300,
    "apple_computer": 1000,
    "casper_computer": 500,
    "monster_computer": 300,
    "airpods": 200,
    "mouse": 50
}

accounts = {"Mehmet": "12345"}  

def manage_account():
    print("Welcome to the e-commerce application.")
    attempts = 0  

    while attempts < 3:  
        choose = input("Enter 1 to log in, 2 to create an account, 3 to delete account: ")

        if choose == "1":
            print("Enter your username and password:")
            username = input("Username: ")
            password = input("Password: ")

            if username in accounts and accounts[username] == password:
                print("Logged in successfully!")
                return True  
            else:
                attempts += 1 
                print("Wrong username or password, please try again.")
                print(f"You have {3 - attempts} attempts left.")
        
        elif choose == "2":
            print("Create a new account:")
            new_username = input("Enter your new username: ")
            new_password = input("Enter your new password: ")

            if new_username in accounts:
                print("This username is already taken.")
            else:
                accounts[new_username] = new_password
                print("Account created successfully!")

        elif choose == "3":
            print("Enter the username and password of the account you want to delete:")
            delete_username = input("Username: ")
            delete_password = input("Password: ")

            if delete_username in accounts and accounts[delete_username] == delete_password:
                del accounts[delete_username]
                print("Account deleted successfully!")
            else:
                print("Wrong username or password, please try again.")

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
        
    print("Too many failed attempts. Exiting the application.")
    return False  

cart = []

def add_to_cart(product_name, price):
    if stock[product_name] > 0:
        print(f"Price: {price}$, In stock: {stock[product_name]}")
        add = input("Add to cart (Y/N): ").strip().lower()
        if add == "y":
            stock[product_name] -= 1
            cart.append(product_name)  
            print(f"Product added to cart. Remaining stock: {stock[product_name]}")
        else:
            print("Product not added to cart.")
    else:
        print(f"Sorry, {product_name.replace('_', ' ').title()} is out of stock.")

def product():
    choose = input("Choose a category: 1-phone, 2-tv, 3-tablet, 4-computer, 5-airpods, 6-mouse ")

    if choose == "1":
        phone = input("Which phone would you like to buy? 1-iphone, 2-samsung, 3-generic ")
        if phone == "1":
            add_to_cart("iphone", 1000)
        elif phone == "2":
            add_to_cart("samsung_phone", 500)
        elif phone == "3":
            add_to_cart("generic_phone", 300)

    elif choose == "2":
        tv = input("Which TV would you like to buy? 1-arcelik, 2-beko, 3-lg ")
        if tv == "1":
            add_to_cart("arcelik_tv", 5000)
        elif tv == "2":
            add_to_cart("beko_tv", 2000)
        elif tv == "3":
            add_to_cart("lg_tv", 1500)

    elif choose == "3":
        tablet = input("Which tablet would you like to buy? 1-ipad, 2-samsung, 3-casper ")
        if tablet == "1":
            add_to_cart("ipad", 1000)
        elif tablet == "2":
            add_to_cart("samsung_tablet", 500)
        elif tablet == "3":
            add_to_cart("casper_tablet", 300)

    elif choose == "4":
        computer = input("Which computer would you like to buy? 1-apple, 2-casper, 3-monster ")
        if computer == "1":
            add_to_cart("apple_computer", 1000)
        elif computer == "2":
            add_to_cart("casper_computer", 500)
        elif computer == "3":
            add_to_cart("monster_computer", 300)

    elif choose == "5":
        add_to_cart("airpods", 200)

    elif choose == "6":
        add_to_cart("mouse", 50)

def checkout(cart, prices):
    if not cart:  
        print("Your cart is empty. Please add products to proceed to checkout.")
        return

    total_price = sum([prices[item] for item in cart])
    print(f"Your total is: {total_price}$")

    payment_method = input("Choose payment method: 1-Credit card 2-Debit card 3-Cash ")

    if payment_method in ["1", "2", "3"]:
        confirm = input(f"Your total is {total_price}$. Do you want to proceed with the payment? (Y/N)").lower()
        if confirm == "y":
            print("Payment successful. Thank you for your purchase!")
        else:
            print("Payment cancelled.")
    else:
        print("Invalid payment method.")

if manage_account(): 
    while True:
        product()  
        more = input("Do you want to buy more products? (Y/N): ").strip().lower()
        if more != "y":
            break

    checkout(cart, prices)
else:
    print("Exiting the application due to failed login.")