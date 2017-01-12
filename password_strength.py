

def check_case_sens(passwd):
    if passwd == passwd.lower() or passwd == passwd.upper():
        return 0
    else: return 1


def check_num_dig(passwd):
    if any(letter.isdigit() for letter in passwd):
        return 1
    return 0


def check_spec_char(passwd):
    if any(letter in ('@','*','_','-','+','%','=','&','`','!','$') for letter in passwd):
        return 1
    return 0


def check_blacklist(passwd):
    if passwd.lower() in ('password', 'mypass', 'ny2017', 'privet', '12345', '123456'):
        return 0
    return 1


def check_user_info(name, passwd):
    if passwd.lower() in list(name):
        return 0
    return 1


def check_comp_name(passwd):
    pass


def check_match_num(passwd):
    pass


def get_password_strength(password):
    pass


if __name__ == '__main__':
    first_name = 'Alex'
    last_name = 'Parker'
    passwd = '123456'
    user_name = first_name + last_name
    print(check_user_info(user_name, passwd))
