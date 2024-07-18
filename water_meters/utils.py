from datetime import datetime


def convert_string_date_to_datetime(string):
    date_list = string.split("-")
    for i in range(len(date_list)):
        date_list[i] = int(date_list[i])
    return datetime(date_list[0], date_list[1], date_list[2])