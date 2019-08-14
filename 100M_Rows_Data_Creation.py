#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Necessary Imports
import pandas as pd
import random
from random import uniform
import string

num_rows = 100000000        # 100M

# Creating time column
#dti = pd.to_datetime(['1/1/2018', np.datetime64('2018-01-01'), datetime.datetime(2018,1,1)])
dti = pd.date_range('2018-01-01', periods=num_rows, freq='s')
data = pd.DataFrame(dti, columns=['time'])

# latLong List function
def listLatLong(minVal, maxVal):
    listlatlong = []
    for _ in range(num_rows):
        listlatlong.append(uniform(minVal, maxVal))
    return listlatlong

# Creating latitude column
latitude = listLatLong(-90, 90)    
data['latitude'] = latitude

# Creating longitude column
longitude = listLatLong(-180, 180)
data['longitude'] = longitude

# Creating station_code column
def randomString(stringLength=6):
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))

station_code = []
for i in range(num_rows):
    station_code.append(randomString())

data['station_code'] = station_code

# Creating station_id column
data.index.name = 'station_id'

data.head()
data.tail()

data.to_csv('TimestampLocations100M.csv')
