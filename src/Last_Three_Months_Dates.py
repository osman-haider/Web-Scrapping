from datetime import datetime, timedelta


def last_three_months_dates_function(current_date):
    last_three_months_dates = []
    last_three_months_dates.append(current_date.strftime("%Y-%m-%d"))

    # Calculate the dates of the last three months
    for i in range(3):
        # Subtract 'i' months from the current date
        current_month = current_date.month - i
        if current_month <= 0:
            current_month += 12
            current_year = current_date.year - 1
        else:
            current_year = current_date.year

        # Calculate the start date of the current month
        start_date_of_current_month = datetime(current_year, current_month, 1)

        # Calculate the end date of the previous month
        end_date_of_previous_month = start_date_of_current_month - timedelta(days=1)

        # Calculate the start date of the previous month
        start_date_of_previous_month = datetime(end_date_of_previous_month.year, end_date_of_previous_month.month, 1)

        # Generate dates for all days of the previous month
        current_day = start_date_of_current_month
        while current_day > start_date_of_previous_month:
            last_three_months_dates.append(current_day.strftime("%Y-%m-%d"))
            current_day -= timedelta(days=1)
    print("Dates of Three Months are Loaded...")
    return last_three_months_dates