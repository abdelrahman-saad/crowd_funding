import user_authentication as AUTH
import GLOBAL as G
import data_files_ops.read_write as rw
import user_ops as user_log

while True:
    G.ALL_USERS = rw.read_data(G.FILE_PATH)
    print('Main Menu')
    print(G.MAIN_MENU)
    choice = input('please enter your choice: ')

    if not choice.isdigit():
        print('please enter a valid input')
        continue

    if choice.strip() == '1':
        AUTH.ask_user_register()
    elif choice.strip() == '2':
        res = AUTH.ask_login()
        if res == G.VALID:
            user_log.user_menu()
    elif choice.strip() == '3':
        continue
    else:
        print("thanks for using the system")
        break
