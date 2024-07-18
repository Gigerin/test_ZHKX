def return_previous_date(month, year):
    if month == 1:
        return (12, year-1)
    else:
        return (month-1, year)