import GLOBAL as G
import data_files_ops.read_write as rw
import user_functions.user_operations as UO


def user_menu():
    print('Welcome back', G.LOGGED_USER[G.JSON_F_NAME])

    while True:
        G.ALL_PROJECTS = rw.read_data(G.PROJECT_PATH)
        print(G.USER_MENU)

        choice = input('please enter your choice: ')

        if not choice.isdigit():
            print('please enter a valid input')
            continue

        if choice == '1':
            UO.view_all(G.ALL_PROJECTS)
        elif choice == '2':
            UO.search_project()
        elif choice == '3':
            UO.create_project()
        elif choice == '4':
            UO.edit_project()
        elif choice == '5':
            UO.delete_project()
        elif choice == '6':
            break
