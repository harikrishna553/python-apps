from datetime import datetime, timedelta

def increase_date_by_n_days(input_date, days_to_increase):
    new_date = input_date + timedelta(days_to_increase)
    return new_date

input_date = datetime(1988, 6, 6)
new_date = increase_date_by_n_days(input_date, 1)

print('input_date -> ', input_date)
print('new_date -> ', new_date)