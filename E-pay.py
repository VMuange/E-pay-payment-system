def create_password():
    done = False
    while not done:
        pass1 = (input("Create new password: "))
        pass2 = (input("Confirm password: "))
        if pass1 == pass2:
            print("Password has been created successfully")
        done = True
        if pass1 != pass2:
            print("Passwords do not match. Please try again.")
            done = False


def create_new_acc():
    (input("Name: "))
    (input("Name of School: "))
    (input("Registration Number: "))
    create_password()
    print("Account set successfully")
    print("Please login")
    login()


def superuser(reg, passw):
    adm_no = "k46"
    password = "password"
    name = "jack"
    if reg != adm_no or passw != password:
        print("Incorrect Password or Registration Number")
        done = False
        while not done:
            print("enter 1 to log in again")
            print("enter 2 to create acc")
            key = input(": ")
            if key == "1":
                login()
                done = True
            elif key == "2":
                create_new_acc()
                done = True
            else:
                print("Invalid choice. Please choose from the given options.")
                done = False
    else:
        print("welcome", name)
        main_menu()


def login():
    reg = input("Enter Registration number: ")
    passw = input("Enter password: ")
    superuser(reg, passw)


def check_balance():
    print("You will receive a confirmation message shortly")


def make_payment():
    input("1. School fees: ")
    input("Enter amount you wish to pay: ")
    input("Enter M-pesa pin: ")
    print("Thank you for using E-pay. You will receive a confirmation message shortly.")


def payment_statement():
    print("Thank you for using E-pay. You will receive a confirmation message shortly.")


def main_menu():
    done = False
    while not done:
        print("1. Check balance.")
        print("2. Make payment.")
        print("3. Request a payment statement.")
        choice = int(input("1, 2, 3: "))
        if choice == 1:
            check_balance()
            done = True
        elif choice == 2:
            make_payment()
            done = True
        elif choice == 3:
            payment_statement()
            done = True
        else:
            print("Invalid choice. Please choose from the given options.")
            done = False


def main():
    dial = input("Dial *777# to proceed: ")
    if dial == "*777#":
        print("1. Create a new account.")
        print("2. Log in.")
        try:
            choice = int(input("1 or 2: "))
        except ValueError:
            print("please only use numbers 1 or 2")
        else:
            if choice == 1:
                create_new_acc()
            elif choice == 2:
                login()
            else:
                print("enter 1 or 2")
    else:
        print("Wrong dial. Kindly try again")


main()
