import random
import numpy as np
from pandas import DataFrame
from pandas import concat
import datetime
from time import time

#pseudo data
current = np.random.rand(20,1)
voltage = current*10
time_stamp_set = np.arange(len(current))[:, np.newaxis]
nominal_current_set = [0.5, 1, 1.5, 2]
nominal_voltage_set = [10, 3.3, 9, 12]
cell_name_set = ['yellow', 'blue', 'green', 'black']
first_name_set = ['Joe', 'Nate', 'Jon', 'Teo']
date = datetime.datetime.now()

# random choices
nominal_current = random.choice(nominal_current_set)
nominal_voltage = random.choice(nominal_voltage_set)
cell_name = random.choice(cell_name_set)
first_name = random.choice(first_name_set)

# data
data_set = DataFrame({'name_student': [first_name],
                    'date': [date],
                    'test_name' : ['battery'],
                    'name_cell' : [cell_name],
                    'nom_volt': [nominal_voltage],
                    'nom_cap': [nominal_current],
                    'timestmp': [time_stamp_set],
                    'current': [current],
                    'voltage': [voltage]})


#preserving column order
column_order = ['name_student', 'date', 'test_name', 'name_cell', 'nom_volt',
                'nom_cap', 'current', 'timestmp', 'voltage']



# saving to CSV in same folder as script

data_set[column_order].to_csv('./generated_data2.csv', index=False)
