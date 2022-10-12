"""
Create random email address
"""

import random
import secrets
import string

DOMAIN = [
    "bheps.com"
]

def generate_email():
    '''Generate random email address'''
    login = ''.join(random.choices(string.ascii_letters + string.digits, k=20))
    domain = random.choice(DOMAIN)
    return f'{login}@{domain}'


def generate_username_filler(number):
    '''Generate usernmae from list plus random string of characters'''
    return ''.join(random.choices(string.ascii_letters + string.digits, k=number))


def generate_random_password():
    '''Return randomly generated password'''
    return ''.join(secrets.choice(string.ascii_letters + string.digits) for i in range(10))
