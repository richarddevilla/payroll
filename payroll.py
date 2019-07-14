import csv
from dateutil.parser import parse
from datetime import datetime, time, timedelta
from subprocess import Popen

dsc_timesheet_headers = [
    'Activity ID',
    'Staff Member',
    'Employment Type',
    'Staff Payroll Payment ID',
    'From',
    'To',
    'Staff Hours',
    'Client',
    'Client Card ID',
    'Activity Name',
    'In Service Km',
    'Notes',
    'Client to Client Km',
    'Notes',
    'Expenses',
    'Billable Expenses'
]


class Roster:

    def __init__(self):
        self.shift = []

    def add_shift(self, data):
        temp_dict = {}
        for item, header in zip(data, dsc_timesheet_headers):
            temp_dict[header] = item
        self.shift.append(temp_dict)

    def total_hours(self):
        hours = 0
        for each in self.shift:
            hours += each['Staff Hours']
        return hours


def valid_import(data):
    """
    Checks if the import matches expected headers
    :param data:
    :return:
    """
    if data == dsc_timesheet_headers:
        return True
    else:
        return False


def data_to_csv(data):
    # load csv file parse data to appropriate types
    with open(data, 'r') as f:
        reader = csv.reader(f)
        csv_data = list(reader)
        if not valid_import(csv_data[0]):
            return False
        for activity in csv_data[1:]:
            # From
            activity[4] = parse(activity[4])
            # To
            activity[5] = parse(activity[5])
            # Staff Hour
            activity[6] = float(activity[6])
            # Activity Name
            activity[9] = activity[9].split(', ')[0]
            # In Service Km
            if activity[10] != '':
                activity[10] = float(activity[10])
            else:
                activity[10] = 0
            # Client to Client KM
            if activity[12] != '':
                activity[12] = float(activity[12])
            else:
                activity[12] = 0
            # Expenses
            activity[14] = activity[14].replace('AUD ', '').replace(',', '.')
            # Billable Expenses
            activity[15] = activity[15].replace('AUD ', '').replace(',', '.')
        return csv_data


def process_data(data):
    staff = {}
    for each in data[1:]:
        if not each[1] in staff:
            staff[each[1]] = Roster()
        staff[each[1]].add_shift(each)


