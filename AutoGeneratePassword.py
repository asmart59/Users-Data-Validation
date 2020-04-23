from UserDataCollection import user_first_name, user_last_name
import random
import string


def random_string(string_lenght):
    password_characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(password_characters) for i in range(string_lenght))


class UserPassword:
    def pass_word(self):
        password = user_first_name[:2] + user_last_name[-2:] + random_string(5)
        return password


auto_generated_password = UserPassword()
auto_generated_password = auto_generated_password.pass_word()
password_display = f'Your password is: {auto_generated_password}'
