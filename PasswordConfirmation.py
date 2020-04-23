from AutoGeneratePassword import password_display
from UserDetails import *
print(password_display)


def password_confirmation():
    while True:
        confirmation = input("To retain the above password, reply Yes; To change your password, reply No: ")
        if confirmation.upper() in ("YES", "NO"):
            break
        print("Sorry, I don't understand that.")
    if confirmation.upper() == "YES":
        print_user_details()

    elif confirmation.upper() == "NO":
        password = input("Type your password: ")
        if len(password) < 7:
            password = input("Your password should contain 7 or more characters: ")
        user_details["Password"] = password
        print_user_details()


password_confirmation()
users = [user_details]
print(users)
