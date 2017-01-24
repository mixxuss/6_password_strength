import getpass, os, argparse


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-b', '--blacklist', help='Path to passwords blacklist file')
    return parser


def check_case_sens(passwd):
    return check_condition(passwd != passwd.lower() or passwd != passwd.upper())


def check_num_dig(passwd):
    return check_condition(any(letter.isdigit() for letter in passwd))


def check_spec_char(passwd):
    return check_condition(any(letter in ('$&+,:;=?@#|\'<>.-^*()%!') for letter in passwd))


def check_blacklist(passwd, blacklist_file):
    if not os.path.exists(blacklist_file):
        return 2
    return check_condition(passwd.lower() not in open(blacklist_file).read())


def check_user_info(username, passwd):
    return check_condition(passwd.lower() not in username.lower())


def check_condition(boolean):
    if boolean:
        return 2
    else:
        return 0


def get_password_strength(password, path):
    result = check_case_sens(password) + check_num_dig(password) + check_spec_char(password) + \
             check_user_info(user, password) + check_blacklist(password, path)
    return result


if __name__ == '__main__':
    parsed_args = create_parser()
    args = parsed_args.parse_args()
    if args.blacklist:
        path = args.blacklist
    else:
        path = ''
    user = input('Username: ')
    password = getpass.getpass('Password: ')
    print('Your password score is', get_password_strength(password, path))
