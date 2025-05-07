# open account
# deposite money
# withdraw money
# remove account
# quit the bank
# accounts[111]['balance']
# accounts = {
#     111 : {
#         'name' : 'harsh',
#         'balance' : 0
#     },

#     222 : {
#         'name' : 'Rahul',
#         'balance' : 0
#     }
# } 


accounts = {}

def create_account():
    name = input('Enter your name: ')
    account_number = int(input('Enter your account number: '))

    if account_number not in accounts:
        accounts[account_number] = {'name' : name, 'balance' : 0}
        print(f'Account created successfully! {accounts[account_number]}')
    else:
        print('Account already exists!')


def deposite_money():
    account_number = int(input("Enter your account number: "))


    if account_number in accounts:
        amount = float(input('Enter the amount: '))
        accounts[account_number]['balance'] += amount
        print(f'Money deposite successfully! {accounts[account_number]}')
    else:
        print('Account does not exist!')

def withdraw_money():
    account_number = int(input('Enter your account number: '))

    if account_number in accounts:
        amount = float(input('Enter the amount: '))
        if amount <= accounts[account_number]['balance']:
            accounts[account_number]['balance'] -= amount
            print(f'Money withdrew successfully! {accounts[account_number]}')
        else:
            print('insufficent amount!')
    else:
        print('account does not exist!')

def remove_account():
    account_number = int(input('enter your account number: '))

    if account_number in accounts:
        accounts.pop(account_number)
        print('Account removed successfully!')
    else:
        print('account does not exist')

def main():
    while True:

        print("""
        press 1 to open account
        press 2 to deposite money
        press 3 to withdraw money
        press 4 to remove account
        press 5 to exit the bank
        """)
        choice = input('Enter your choice: ')

        if choice == '1':
            create_account()
        elif choice == '2':
            deposite_money()
        elif choice == '3':
            withdraw_money()
        elif choice == '4':
            remove_account()
        else:
            break


main()
