import getpass, os, argparse


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-b', '--blacklist', help='Path to passwords blacklist file')
    return parser


def check_case_sens(passwd):
    return yes_or_no(passwd != passwd.lower() or passwd != passwd.upper())


def check_num_dig(passwd):
    return yes_or_no(any(letter.isdigit() for letter in passwd))


def check_spec_char(passwd):
    return yes_or_no(any(letter in ('$&+,:;=?@#|\'<>.-^*()%!') for letter in passwd))


def check_blacklist(passwd, blacklist_file):
    if not os.path.exists(blacklist_file):
        return 2
    return yes_or_no(passwd.lower() not in open(blacklist_file).read())


def check_user_info(username, passwd):
    return yes_or_no(passwd.lower() not in username.lower())


def yes_or_no(boolean):
    # Для проверяющего: если функция получает False - то возврщает 0, если получает True - 2
    return boolean * 2


def get_password_strength(password, path):
    # Для проверяющего: если мы находим пароль в блеклисте - то оцениваем его в 0, для этого и умножаем на результат
    # функции check_blacklist
    result = check_case_sens(password) + check_num_dig(password) + check_spec_char(password) + \
             check_user_info(user, password) * check_blacklist(password, path)
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
