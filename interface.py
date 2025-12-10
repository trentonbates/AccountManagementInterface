from os import system
from csv import DictReader
from checking import Checking
from savings import Savings
from credit import Credit
from customer import Customer

customers_dict = dict()

def importData():
    global customers_dict
    file_loc = input('Enter the local path of the data file: ')

    with open(file_loc, 'r') as customers:
        customers_list = list(DictReader(customers))
        customers.close()

    for customer in customers_list:
        temp_username = customer['username']
        temp_checking = Checking(customer['checking_id'], float(customer['checking_balance']))
        temp_savings = Savings(customer['savings_id'], float(customer['savings_balance']))
        temp_credit = Credit(customer['credit_id'], float(customer['credit_balance']), float(customer['credit_limit']))
        customers_dict[customer['username']] = Customer(temp_username, temp_checking, temp_savings, temp_credit)

    print(customers_dict)

def viewCustomers():
    global customers_dict
    for key in customers_dict:
        print(customers_dict[key])

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

    while user_choice < 1 or user_choice > 8:
        print('1. Import customer data\n'
              + '2. View all customers\n'
              + '3. Make a deposit\n'
              + '4. Make a withdrawal\n'
              + '5. Add charge to credit account\n'
              + '6. Make payment to credit account\n'
              + '7. Exit & export data\n')
        user_choice = int(input('Enter a number from 1-7: '))
        
        if user_choice == 1:
            importData()
            user_choice = -1
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
        elif user_choice == 7:
            print('Goodbye!')
            exit()
        else:
            user_choice = int(input('Please enter a number between 1-7: '))

accountManagementInterface()