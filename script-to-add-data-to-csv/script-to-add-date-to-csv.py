import pandas as pd
import csv
from datetime import datetime, timedelta
df = pd.read_csv('../dataset/Nasa/trainupdated.csv')

def convert_date_to_string(date_val):
    return date_val.strftime("%Y-%m-%d %H:%M:%S")

def convert_string_to_date(date_str):
    return datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")

prev_unit_nr = 1
initial_date = '2022-06-01 01:00:00'
date_to_add = '2022-06-01 01:00:00'
# example format: 2016-07-01 02:00:00
# date_val = datetime.strptime(date_to_add, "%Y-%m-%d %H:%M:%S")
date_val = convert_string_to_date(date_to_add)

print("date_val: ", date_val)
date_str_test = convert_date_to_string(date_val)
print("date_str_test: ", date_str_test)
df['date'] = df['unit_nr']

for index, value in enumerate(df['unit_nr']):
    if value != prev_unit_nr:
        print("reset the date column for this index to first date like June 1")
        date_to_add = initial_date
        df['date'][index] = date_to_add
    else:
        print("increment the date to the next day")
        date_obj = convert_string_to_date(date_to_add)
        # increment date
        date_to_add = (datetime.strptime(date_to_add, '%Y-%m-%d %H:%M:%S') + timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')
        df['date'][index] = date_to_add
    
    prev_unit_nr = value
    # print("index: ", index, "value: ", value)
df.to_csv("../dataset/Nasa/trainupdated_with_date.csv",index=False)


