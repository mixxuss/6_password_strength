import getpass


def check_case_sens(passwd):
    # Case sens checking
    if passwd == passwd.lower() or passwd == passwd.upper():
        return 0
    return 2


def check_num_dig(passwd):
    # Digit contain checking
    if any(letter.isdigit() for letter in passwd):
        return 2
    return 0


def check_spec_char(passwd):
    # Special characters cheking
    if any(letter in ('$&+,:;=?@#|\'<>.-^*()%!') for letter in passwd):
        return 2
    return 0


def check_blacklist(passwd):
    # Blacklist checking
    if passwd.lower() in open('top100_pass.txt').read():
        return 0
    return 2


def check_user_info(username, passwd):
    # Username match checking
    if passwd.lower() in username.lower():
        return 0
    return 2


def get_password_strength(password):
    # Execute other functions and return strength score
    result = check_case_sens(password) + check_num_dig(password) + check_spec_char(password) + check_user_info(user, password)* check_blacklist(password)
    return result


if __name__ == '__main__':
    user = input('Username: ')
    password = getpass.getpass('Password: ')
    print('Your password score is:', get_password_strength(password))
