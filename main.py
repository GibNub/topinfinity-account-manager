"""
Main file
"""
import random
import time
import os

from account import Account
import credentials


DIR = 'pfps/'


accounts = []
bar = f"{'='*30}\n"
message = f'''{bar}Type a number
1: Create topic
2: Create item in a topic (only one)
3: Rate an item
4: Change pfp
{bar}
>>> '''


def create_accounts():
    '''Creates accounts with unique filler from list of usernames'''
    # Get usernames
    with open('username.txt', 'r') as file:
        usernames = file.read().splitlines()
    random.shuffle(usernames)
    i = 0
    # Create accounts, bypass email
    for name in usernames:
        username = f'{credentials.generate_username_filler(20-len(name))}{name}'
        password = credentials.generate_random_password()
        account = Account(username, password)
        Account.create_account(account)
        accounts.append(account)
        i += 1
        print(f'\rCreated {i} account(s)', end='', flush=True)


def create_topic():
    '''Create a topic with each account'''
    title = input(f'\nCreate topic\n{bar}Topic title\n>>> ')
    desc = input(f'{bar}Topic description\n>>> ')
    i = 0
    for account in accounts:
        account.create_topic(title, desc)
        i += 1
        print(f'\rCreated {i} topic(s)', end='', flush=True)
    print('\n\nTopic Creation Complete\n')


def create_item():
    '''Create one item for a topic, random account chosen'''
    topic_id = int(input(f'\nCreate item\n{bar}Enter topic id\n>>> '))
    name = input(f'{bar}Name of item\n>>> ')
    Account.change_topic_id(topic_id)
    account = random.choice(accounts)
    account.create_item(name)
    print('\n\nItem creation complete\n')


def rate_item():
    '''Rate an item with each account'''
    item_id = int(input(f'\nRate item\n{bar}Enter item id\n>>> '))
    rating = input(f'{bar}Rating (accepts 1-5)\n>>> ')
    Account.change_rate_id(item_id)
    i = 0
    for account in accounts:
        account.rate_item(rating)
        i += 1
        print(f'\nRated {i} time(s)', end='', flush=True)
    print('\n\nRating complete\n')


def change_pfp():
    '''Change pfp for all users from randomly chosen pfp in directory'''
    # Check if pfps folder exists
    if not os.path.exists(DIR):
        os.makedirs(DIR)
        print('\npfp folder created')
    i = 0
    input(f'''
{bar}Place profile pictures inside pfps folder, then press enter once complete
{bar}>>> ''')
    for account in accounts:
        pfp_name = random.choice(os.listdir(DIR))
        directory = os.path.join(DIR, pfp_name)
        account.change_pfp(directory)
        i += 1
        print(f'\nPfp changed for {i} account(s)', end='', flush=True)
    print('\nPfp change complete\n')


def main():
    """
    Main function
    """
    print('Creating accounts...')
    create_accounts()
    print('\nAccounts creation complete!')
    while True:
        time.sleep(0.5)
        choice = input(message)
        if choice == '1':
            create_topic()
        elif choice == '2':
            create_item()
        elif choice == '3':
            rate_item()
        elif choice == '4':
            change_pfp()
        else:
            print('\n[Invalid Input]\n')


if __name__ == '__main__':
    main()
