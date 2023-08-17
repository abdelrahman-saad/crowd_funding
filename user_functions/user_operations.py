from datetime import datetime
import re
import GLOBAL as G
from tabulate import tabulate
import data_files_ops.read_write as rw


# https://pypi.org/project/tabulate/


def view_all(table):
    if len(table) != 0:
        # Extract keys from the first dictionary to use as headers
        headers = table[0].keys()

        # Create a list of lists for tabulation
        table_data = [[d[key] for key in headers] for d in table]
        print(tabulate(table_data, headers=headers, tablefmt='grid'))
    else:
        print('Projects are empty right now')


def create_project():
    while True:
        print('please enter non empty values \n')
        title = input('please enter project title : ')
        details = input('please enter project details : ')
        target = input('please enter project target : ')
        start_date = input('please enter project start date (dd-mm-yyyy) : ')
        end_date = input('please enter project end date (dd-mm-yyyy): ')
        user_email = G.LOGGED_USER[G.JSON_EMAIL]

        if (
                title.strip() != 0
                and details.strip() != 0
                and (target != 0 or target.isnumeric())
                and start_date.strip() != 0 and end_date.strip() != 0
                and validate_date(start_date) == G.VALID
                and validate_date(end_date) == G.VALID
        ):
            data = {
                G.JSON_TITLE: title,
                G.JSON_DETAILS: details,
                G.JSON_TARGET: target,
                G.JSON_START_DATE: start_date,
                G.JSON_END_DATE: end_date,
                G.JSON_USER: user_email,
            }
            rw.append_data(data, G.PROJECT_PATH)
            print('project inserted successfully')
            return G.VALID


def edit_project():
    answer = input('please enter the project title: ')
    if answer.strip() != 0:
        index = 0
        found = False
        for project in G.ALL_PROJECTS:
            if project[G.JSON_TITLE] == answer:
                found = True
                break
            index += 1
        if not found:
            print("The project title is not found")
        else:
            if G.ALL_PROJECTS[index][G.JSON_USER] != G.LOGGED_USER[G.JSON_EMAIL]:
                print('You cannot edit this project as it does not belong to you')
                return
            title = input('please enter new project title : ')
            details = input('please enter new project details : ')
            target = input('please enter new project target : ')
            start_date = input('please enter new project start date : ')
            end_date = input('please enter new project end date : ')
            if (
                    title.strip() != 0
                    and details.strip() != 0
                    and (target != 0 or not target.isnumeric())
                    and start_date.strip() != 0 and end_date.strip() != 0
            ):
                G.ALL_PROJECTS[index][G.JSON_TITLE] = title
                G.ALL_PROJECTS[index][G.JSON_DETAILS] = title
                G.ALL_PROJECTS[index][G.JSON_TARGET] = title
                G.ALL_PROJECTS[index][G.JSON_START_DATE] = title
                G.ALL_PROJECTS[index][G.JSON_END_DATE] = title

                rw.write_data(G.ALL_PROJECTS, G.PROJECT_PATH)


def delete_project():
    answer = input('please enter the project title that you want to delete: ')
    if answer.strip() != 0:
        index = 0
        found = False
        for project in G.ALL_PROJECTS:
            if project[G.JSON_TITLE] == answer:
                found = True
                break
            index += 1
        if not found:
            print("The project title is not found")
        else:
            if G.ALL_PROJECTS[index][G.JSON_USER] != G.LOGGED_USER[G.JSON_EMAIL]:
                print('You cannot edit this project as it does not belong to you')
                return
            else:
                G.ALL_PROJECTS.pop(index)
                rw.write_data(G.ALL_PROJECTS,G.PROJECT_PATH)


def validate_date(date: str):
    if re.match(r'^\d{2}-\d{2}-\d{4}$', date):
        return G.VALID  # if the expression matches
    print('Please enter a valid date as shown')
    return G.NOT_VALID  # if the expression is not valid


def search_project():
    date_filter = input('please enter a date (dd-mm-yyyy) : ')
    if date_filter.strip() == 0 and validate_date(date_filter):
        return

    # convert user input into date
    user_date = datetime.strptime(date_filter, '%d-%m-%Y')

    # Filter the list of dictionaries based on user input
    filtered_data = [
        project for project in G.ALL_PROJECTS
        if (datetime.strptime(project['start_date'], '%d-%m-%Y') <= user_date
            <= datetime.strptime(project['end_date'], '%d-%m-%Y'))
    ]
    if len(filtered_data) != 0:
        # Extract keys from the first dictionary to use as headers
        headers = filtered_data[0].keys()

        # Create a list of lists for tabulation
        table_data = [[d[key] for key in headers] for d in filtered_data]
        print(tabulate(table_data, headers=headers, tablefmt='grid'))
    else:
        print('Projects are empty right now')
