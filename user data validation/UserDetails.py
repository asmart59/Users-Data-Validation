from AutoGeneratePassword import auto_generated_password
from UserDataCollection import *
user_details = {
         "Name": user_first_name + ' ' + user_last_name,
         "Email": user_email,
         "Password": auto_generated_password}


def print_user_details():
    print(f'Name: {user_details["Name"]}')
    print(f'Email: {user_details["Email"]}')
    print(f'Password: {user_details["Password"]}')
