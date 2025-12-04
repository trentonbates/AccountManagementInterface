from customer import Customer
from sys import exit
from os import system

def importData():
    pass

def viewCustomers():
    pass

def deposit():
    pass

def withdraw():
    pass

def creditCharge():
    pass

def creditPayment():
    pass

def accountManagementInterface():
    system('cls')
    user_choice = -1
    print('Welcome to the Account Management Interface!\n')

    while user_choice != 7:
        print('1. Import customer data\n'
              + '2. View all customers\n'
              + '3. Make a deposit\n'
              + '4. Make a withdrawal\n'
              + '5. Add charge to credit account\n'
              + '6. Make payment to credit account\n'
              + '7. Exit\n')
        input('Enter a number from 1-7: ')
        
        if user_choice == 1:
            importData()
        elif user_choice == 2:
            viewCustomers()
        elif user_choice == 3:
            deposit()
        elif user_choice == 4:
            withdraw()
        elif user_choice == 5:
            creditCharge()
        elif user_choice == 6:
            creditPayment()
        else:
            user_choice = ('Please enter a number between 1-7: ')

    print('Goodbye!')
    exit()

accountManagementInterface()