import pandas as pd

# read the csv
input_name = "heart.csv"
df = pd.read_csv(input_name, parse_dates=["dateTime"], infer_datetime_format=True)
# csv is read, do operations

# adds an int column based on hour ranges; range(24)
def addHourCol(output_name):
    d = []
    for date in df['dateTime']:
        d.append(date.hour)

    new_df = pd.DataFrame({'hora': d})

    df['hora'] = new_df
    df.to_csv(output_name, index=False)

# adds an int column based on weekday; {'mon'-'sun': range(6)}
def addWeekdayCol(output_name):
    d = []
    for date in df['dateTime']:
        d.append(date.weekday())

    new_df = pd.DataFrame({'weekday': d})

    df['weekday'] = new_df
    df.to_csv(output_name, index=False)

# adds a boolean column based on wether date was business period(true) or vacation(false)
def addWorkCol(output_name):
    d = []
    for date in df['dateTime']:
        if date.month == 12 and date.day > 15:
            d.append(False)
        elif date.month == 1:
            d.append(False)
        elif date.month == 2 and date.day < 18:
            d.append(False)
        else:
            d.append(True)

    new_df = pd.DataFrame({'working': d})

    df['working'] = new_df
    df.to_csv(output_name, index=False)


'''
other possible columns:
- day period (morning, afternoon, night, dawn)
'''
