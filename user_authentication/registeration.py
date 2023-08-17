import re
import GLOBAL as G  # this holds data of globally used variables
import data_files_ops.read_write as rw


def register_user(first_name: str, last_name: str, email: str,
                  password: str, conf_pass: str, mobile: str):
    if password != conf_pass:
        return G.PASSWORD_MISMATCH
    if validate_mobile(mobile) == G.NOT_VALID:
        return G.NOT_VALID
    inserted_data = {
        G.JSON_F_NAME: first_name,
        G.JSON_L_NAME: last_name,
        G.JSON_EMAIL: email,
        G.JSON_PASSWORD: password,
        G.JSON_MOBILE: mobile
    }
    rw.append_data(inserted_data, G.FILE_PATH)
    return G.VALID


def ask_user_register():
    while True:
        first_name = input('please enter your first name :')
        last_name = input('please enter your last name :')
        email = input('please enter your email :')
        password = input('please enter your password :')
        conf_password = input('please enter your password again :')
        mobile_number = input('please enter your mobile number :')

        if (
            (first_name.isalpha() and first_name.strip() != 0)
                and (last_name.isalpha() and last_name.strip() != 0)
                and (email.strip() != 0)
                and (password.strip() != 0) and (conf_password.strip() != 0)
                and (mobile_number.isnumeric())
        ):
            var = register_user(first_name,last_name,email,password,conf_password,mobile_number)
            if var == G.VALID:
                print('User Successfully Created')
                return G.VALID
            elif var == G.NOT_VALID:
                return 'please enter a valid mobile number '
            elif var == G.PASSWORD_MISMATCH:
                return 'Please make sure passwords are matched'
        print('Please insert non empty values ')


def validate_mobile(mobile_number: str):
    # ^01[0125][0-9]{8}$
    if not (str(mobile_number).isnumeric()):
        return G.STR_NOT_ALPHA

    if re.match(r'^01[0125][0-9]{8}$', mobile_number):
        return G.VALID  # if the expression matches
    print('Please enter a valid mobile number')
    return G.NOT_VALID  # if the expression is not valid
