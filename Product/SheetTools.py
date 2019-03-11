import gspread
from oauth2client.service_account import ServiceAccountCredentials

import ActivityDataObject

template = [
    ['Admin', '', '', '', '', ''],
    ['', '', '', '', '', ''],
    ['STATISTICS', '', '', '', 'Averages', ''],
    ['', 'Distance', 'Time', 'Count', 'Distance', 'Time'],
    ['TOTAL', '0', '0', '0', '0', '0'],
    ['SKI', '0', '0', '0', '0', '0'],
    ['BIKE', '0', '0', '0', '0', '0'],
    ['RUN', '0', '0', '0', '0', '0'],
    ['', '', '', '', '', ''],
    ['ACTIVITIES', '', '', '', '', ''],
    ['Sport', 'Title', 'Time', 'Distance', 'Description', 'ID']
]


def open_database():
    scope = [
        'https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive'
    ]
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        'client_secret.json',
        scope
    )  # Retrieves credentials from client_secret.json file
    gc = gspread.authorize(credentials)  # Authorizes GSpread
    database = gc.open("KTrackerDatabase")  # Opens KTrackerDatabase sheet
    return database


def check_user(user):
    sheet = open_database()  # Retrieves the database

    worksheets = sheet.worksheets()  # Gets a list of all users

    if user in worksheets:  # Checks if the user is in the list
        return True
    else:
        return False


def get_user_data(user):
    try:
        worksheet = get_worksheet(user)  # Gets the user's worksheet
        data = worksheet.get_all_values()  # Parses into a 2D array
        return data
    except ValueError:
        return 1


def get_password(user):
    data = get_user_data(user)  # Retrieves a user's worksheet as a 2D array

    password = data[0][0]  # Gets the password from the array

    return password


def get_stats(user):
    data = get_user_data(user)  # Retrieves a user's worksheet as a 2D array

    stats = [[] for _ in range(4)]  # Generates a 2D array for statistics

    for i in range(4, 8):
        for j in range(1, 6):
            stats[i-4].append(data[i][j])  # Adds the statistics to the array

    return stats


# noinspection PyTypeChecker
def get_activities(user):
    data = get_user_data(user)  # Retrieves a user's worksheet as a 2D array

    num_activities = len(data) - 11  # Int value of number of activities for the user

    activities = [[] for _ in range(num_activities)]  # Generates 2D array for activities

    for i in range(11, 11+num_activities):  # Copies activities from worksheet
        for j in range(0, 6):
            activities[i-11].append(data[i][j])

    for i in range(len(activities)):  # Converts all the activities into Activity objects
        activities[i] = ActivityDataObject.ActivityData(activities[i])

    return activities


def add_activity(user, a):
    data = get_worksheet(user)  # Retrieves a user's worksheet

    data.insert_row(a, 12)  # Adds the activity as a new row on the sheet


def edit_activity(user, new, old):
    data = get_user_data(user)  # Retrieves a user's worksheet as a 2D array

    num_activities = len(data) - 11  # Int value of number of activities for the user

    for i in range(11, 11+num_activities):  # Checks if the activity remained the same
        same = True
        for j in range(0, 6):
            if not data[i][j] == old[j]:  # Compares activity to all saved in Database
                same = False

        if same:  # If the activity had been edited
            data = get_worksheet(user)
            data.delete_row(i+1)  # Removes the old activity
            add_activity(user, new)  # Adds the edited version
            break


def delete_activity(user, activity_id):
    sheet = get_worksheet(user)
    data = get_user_data(user)

    num_activities = len(data) - 11  # Int value of number of activities for the user

    for i in range(11, 11+num_activities):  # Searches for the matching timestamp
        if int(data[i][5]) == activity_id:
            sheet.delete_row(i+1)  # Deletes the matching activity
            break


def add_user(username, password1, password):
    try:  # If the user exists, does nothing
        get_user_data(username)
        return 1
    except ValueError:
        if password == password1:  # Checks if the passwords match
            database = open_database()
            database.add_worksheet(
                title=username,
                rows='100',
                cols='10'
            )  # Adds a worksheet for the new user
            worksheet = database.worksheet(username)  # Retrieves the new worksheet
            data = template  # copies the saved template for users
            data[0][0] = password  # changes the password cell
            for i in range(len(data)-1, -1, -1):
                worksheet.insert_row(data[i], index=1)  # Adds the template to the sheet
            return 2
        return 3


def get_worksheet(user):
    database = open_database()  # Opens the database
    worksheet = database.worksheet(user)  # Retrieves the user's worksheet
    return worksheet


def get_name(user):
    data = get_user_data(user)  # Retrieves a user's worksheet as a 2D array
    return data[0][1]
