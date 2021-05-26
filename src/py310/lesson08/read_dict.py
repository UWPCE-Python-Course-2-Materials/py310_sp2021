import csv


with open('hrdata.csv') as csvfile:
    hrcsv = csv.DictReader(csvfile)
    row_number = 0

    for row in hrcsv:
        print(f"row {row_number}")
        row_number += 1

        for key, value in row.items():
            print(f"{key=} {value=}")


'''
import pandas as pd
pd.read_csv('hrdata.csv', index_col=0, header=None, squeeze=True).to_dict()
'''
