#2- Data of Register for the Customer 
#---------------------------------------------

#import welcome
import welcome


def customer():
    print(welcome.welcome())  # Display the welcome message from the welcome module
    name = input("Please enter your name: ")
    email = input("Please enter your email: ")
    while True:
        phone = input("Please enter your phone number: ").strip()
        if phone.isdigit():
            phone = int(phone)
            break
        print("\n*** Invalid input. Please enter only digits for your phone number.***")
    return name, email, phone

if __name__ == "__main__":
    customer_data = customer()
    print("\nCustomer Data:\n", customer_data)

