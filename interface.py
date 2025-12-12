from sys import exit
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

def viewCustomers():
    global customers_dict
    for key in customers_dict.keys():
        print(customers_dict[key])

def balanceChange(deposit = True):
    global customers_dict
    customer_choice = ''
    account_choice = ''
    dollar_amount = 0.0

    while customer_choice not in customers_dict.keys():
        for key in customers_dict.keys():
            print(key)

        customer_choice = input('Select a customer: ')

    while account_choice.lower() not in ['checking', 'savings']:
        account_choice = input('Checking or Savings? ')

    while dollar_amount <= 0.0:
        if deposit:
            dollar_amount = int(input('Enter amount to deposit: '))
        else:
            dollar_amount = int(input('Enter amount to withdraw: '))

    if account_choice.lower() == 'checking':
        customers_dict[customer_choice].checking.deposit(dollar_amount)
    else:
        customers_dict[customer_choice].checking.withdraw(dollar_amount)

def accountManagementInterface():
    system('cls')
    user_choice = -1
    print('Welcome to the Account Management Interface!\n')

    while user_choice < 1 or user_choice > 7:
        print('1. Import customer data\n'
              + '2. View all customers\n'
              + '3. Make a deposit\n'
              + '4. Make a withdrawal\n'
              + '5. Add charge to credit account\n'
              + '6. Make payment to credit account\n'
              + '7. Exit & export data\n')
        
        while user_choice not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            user_choice = input('Enter a number from 1-7: ')
        
        user_choice = int(user_choice)
        print()
        
        if user_choice == 1:
            importData()
            print()
        elif user_choice == 2:
            viewCustomers()
        elif user_choice == 3:
            balanceChange()
        elif user_choice == 4:
            balanceChange(False)
        elif user_choice == 5:
            pass
        elif user_choice == 6:
            pass
        elif user_choice == 7:
            print('Goodbye!')
            exit()
        
        user_choice = -1

accountManagementInterface()