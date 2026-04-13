#3 - Destiny List of Items - Brasil

# importing the customer module to use its functions and data
import customer


customer_data = customer.customer()  # Get customer data from the customer module

def destiny():
    print("\nDear Customer: " + customer_data[0] +"\n" "\nPlease!, select your destination? \n")
    destination = """
                     | # |  Destinaty  | Time Out | Price | Gate | Time Estimate In |
                     |--------------------------------------------------------------|
                     | 1 | Curitiba    |  08:00    | $100  |  A1  |    10:00        |
                     | 2 | Porto Alegre|  09:00    | $150  |  A2  |    11:30        |
                     | 3 | Cascavel    |  10:00    | $200  |  A3  |    12:00        |
                     | 4 | Toledo      |  11:00    | $120  |  A4  |    13:00        |
                     |--------------------------------------------------------------|"""
    print(destination)
destiny()

def destiny_selection():
    print("\nPlease select your destination by entering the corresponding number (1-4): \n ")
    match destiny_choice := input().strip():
        case '1':
            print("\nYou have selected Curitiba as your destination.")
            Curitiba_Ticket = int(input("\nPlease enter the number of tickets you want to purchase for Curitiba: "))

            print(f"\nDear customer: {customer_data[0]}\nYou have purchased: {Curitiba_Ticket} tickets for Curitiba.")

            Curitiba_Ticket_Price = 101.10
            Price_Final_Curitiba = Curitiba_Ticket * Curitiba_Ticket_Price

            print(f"\nThe total price for your purchase is: ${Price_Final_Curitiba:.2f}")

            print("\nRemember that the out of your trip is to the 08:00 hrs in the Gate A1, and the estimated time of arrival is 10:00 hrs.")
            return 1
        
        case '2':
            print("\nYou have selected Porto Alegre as your destination.")
            return 2
        
        case '3':
            print("\nYou have selected Cascavel as your destination.")
            return 3
        
        case '4':
            print("\nYou have selected Toledo as your destination.")
            return 4
        case _:
            print("\n*** Invalid selection. Please enter a number between 1 and 4. ***")
            return destiny_selection()  # Recursively call the function until a valid input is received
destiny_choice = destiny_selection()

print(f"\nDear Customer: {customer_data[0]} Thanks for traveling with us \n*****Good Travel!  :) *****\n")            

