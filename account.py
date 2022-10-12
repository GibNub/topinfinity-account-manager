"""
Module to handle account as object
"""

# import re
# from time import sleep

import requests
import credentials
# from onesecmail import OneSecMail


DOMAIN = 'https://topinfinity.blackdahu.com'
HTTPS_REGEX = r'\b((?:https?://)?(?:(?:www\.)?(?:[\da-z\.-]+)\.(?:[a-z]{2,6})|(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)|(?:(?:[0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|(?:[0-9a-fA-F]{1,4}:){1,7}:|(?:[0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|(?:[0-9a-fA-F]{1,4}:){1,5}(?::[0-9a-fA-F]{1,4}){1,2}|(?:[0-9a-fA-F]{1,4}:){1,4}(?::[0-9a-fA-F]{1,4}){1,3}|(?:[0-9a-fA-F]{1,4}:){1,3}(?::[0-9a-fA-F]{1,4}){1,4}|(?:[0-9a-fA-F]{1,4}:){1,2}(?::[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:(?:(?::[0-9a-fA-F]{1,4}){1,6})|:(?:(?::[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(?::[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(?:ffff(?::0{1,4}){0,1}:){0,1}(?:(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])|(?:[0-9a-fA-F]{1,4}:){1,4}:(?:(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])))(?::[0-9]{1,4}|[1-5][0-9]{4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5])?(?:/[\w\.-]*)*/?)\b'

class UserData:
    '''
    Store userdata in object
    '''
    def __init__(self, username, password) -> None:
        # Generate email and userdata
        self.username = username
        self.password = password
        # self.mailbox = OneSecMail.from_address(credentials.generate_email())
        self.session = requests.Session()
        # self.mail_address = self.mailbox.address
        self.creds = {
            'username': self.username,
            'password': self.password,
            'confpassword': self.password,
            'email': f'{credentials.generate_username_filler(9)}@gmail.com'
        }


class Account:
    '''
    Create and manage an account in TopInfinity
    '''
    rate_id = None
    topic_id = None

    def __init__(self, username, password) -> None:
        self.userdata = UserData(username, password)
        self.topic = None
        self.topic_item = None
        self.item_rate = None


    def create_account(self):
        '''
        Creates account with userdata (only use once)
        '''
        # Create account
        self.userdata.session.get(url=f'{DOMAIN}')
        self.userdata.session.post(url=f'{DOMAIN}/signup', data=self.userdata.creds)
        # Confirm account
        # Get email message from userdata email address
        # Get contents and find confirmation URL
        # Send get request with found url
        # sleep(5)
        # self.userdata.session.get(
        #     re.findall(
        #         HTTPS_REGEX, (self.userdata.mailbox.get_message_as_dict(
        #                 self.userdata.mailbox.get_messages()[0]
        #                 )
        #             )['body']
        #         )[0]
        #     )


    def create_topic(self, title, description):
        '''
        Create topic
        '''
        self.topic = {
            'title': title,
            'description': description
        }
        self.userdata.session.post(url=f'{DOMAIN}/addtopic', data=self.topic)


    def create_item(self, name):
        '''
        Create an item for a specified topic
        '''
        self.topic_item = {
            'itemname': name
        }
        self.userdata.session.get(url=f'{DOMAIN}/topic/{Account.topic_id}')
        self.userdata.session.post(url=f'{DOMAIN}/additem', data=self.topic_item)


    def rate_item(self, rating):
        '''
        Rate an item in a topic with value
        '''
        self.item_rate = {
            f'rating.{Account.rate_id}': rating
        }
        self.userdata.session.post(url=f'{DOMAIN}/rate/{Account.rate_id}', data=self.item_rate)


    @classmethod
    def change_rate_id(cls, new_id):
        '''
        Change rating id for all instances
        '''
        cls.rate_id = new_id


    @classmethod
    def change_topic_id(cls, new_id):
        '''
        Change topic id for all instances
        '''
        cls.topic_id = new_id


    def __del__(self):
        print(f'Account {self.userdata.username} is no longer available for access')
