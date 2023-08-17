"""
    File path
"""

FILE_PATH = 'data_dir/users.json'
PROJECT_PATH = 'data_dir/projects.json'

"""
    ERRORS keys
"""

PASSWORD_MISMATCH = 'PASSWORD_MISSMATCH'
STR_NOT_ALPHA = 'STR_NOT_ALPHA'
VALID = 'VALID'
NOT_VALID = 'NOT_VALID'
EMPTY = 'EMPTY'

"""
    USER JSON keys
"""
JSON_F_NAME = 'first_name'
JSON_L_NAME = 'last_name'
JSON_EMAIL = 'email'
JSON_PASSWORD = 'password'
JSON_MOBILE = 'mobile_phone'

"""
    USER JSON keys
"""
JSON_TITLE = 'title'
JSON_DETAILS = 'details'
JSON_TARGET = 'target'
JSON_START_DATE = 'start_date'
JSON_END_DATE = 'end_date'
JSON_USER = 'user'

"""
    Global List of Dicts
"""
ALL_USERS = [{}]
LOGGED_USER = {}
LOGGED_USER_INDEX = 0
ALL_PROJECTS = [{}]

"""
    Menu
"""

MAIN_MENU = """
1 - register
2 - log in
3 - show menu again
4 - exit
"""

"""
    User Functions
"""

USER_MENU = """
1 - view all projects
2 - search for a project using date
3 - create a project
4 - edit a project
5 - delete a project
6 - logout
"""

