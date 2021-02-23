#!/usr/bin/python
import pandas as pd
from exif import Image as im
from PIL import Image
from PIL.ExifTags import TAGS
import os
import numpy as np
import matplotlib

directory = "Downloads/Field\ trip\ images/"  # path to pictures
tag_list = ['make', 'model', 'datetime', 'x_resolution', 'y_resolution', 'gps_altitude', 'gps_img_direction',
            'gps_speed']
value_list = []
value = []
for filename in os.listdir(directory):
    if filename.endswith(".JPG"):
        with open(os.path.join(directory, filename), 'rb') as image_file:
            img = im(image_file)

        if ('make' in dir(img)):
            value.append(img.make)
        else:
            value.append(np.nan)
        if ('model' in dir(img)):
            value.append(img.model)
        else:
            value.append(np.nan)
        if ('datetime' in dir(img)):
            value.append(img.datetime)
        else:
            value.append(np.nan)
        if ('x_resolution' in dir(img)):
            value.append(img.x_resolution)
        else:
            value.append(np.nan)
        if ('y_resolution' in dir(img)):
            value.append(img.y_resolution)
        else:
            value.append(np.nan)
        if ('gps_altitude' in dir(img)):
            value.append(img.gps_altitude)
        else:
            value.append(np.nan)
        if ('gps_img_direction' in dir(img)):
            value.append(img.gps_img_direction)
        else:
            value.append(np.nan)
        if ('gps_speed' in dir(img)):
            value.append(img.gps_speed)
        else:
            value.append(np.nan)
        value_list.append(value)
        value = []

df = pd.DataFrame(value_list, columns=tag_list)

# df.to_csv('test.csv')  # export to csv


df.to_csv('test.csv')  # export to csv
print(df)

# returns the number of pictures we pulled metadata from
print(len(df.index), 'Pictures processed')

# any missing data?
print(df.isna().sum().sum(), 'Missing data points total')

# any missing data points: make, model, datetime, x_resolution, y_resolution, gps_altitude, gps_img_direction, gps_speed
for key in df:
    print(df[key].isna().sum(), 'Missing', key, 'data points')

# what date had the most pictures taken?
print('Date with the most pictures taken', df['datetime'].value_counts().idxmax())
# least?
print('Date with the least pictures taken', df['datetime'].value_counts().idxmin())

# sort data frame by column
sorted_df = df.sort_values('datetime')
print(sorted_df)

# find frequency of metadata, disply in histogram
hist = df['x_resolution'].hist(bins=20)
matplotlib.pyplot.show()

# Number of pictures in day vs night
time = []
datetime = df['datetime']
for entry in datetime:
    split = entry.split()
    times = split[1].split(':')
    hour = times[0]
    if (int(hour) > 5 and int(hour) < 19):
        time.append(1)
    else:
        time.append(0)
df['Daytime'] = time
hist = df['Daytime'].hist(bins=10)
matplotlib.pyplot.show()

# Number of pictures per month
month = []
date_month = datetime
date_month.to_pydatetime()
for mon in date_month:
    if (int(mon.month) == 1):
        month.append('January')
    elif (int(mon.month) == 2):
        month.append('February')
    elif (int(mon.month) == 3):
        month.append('March')
    elif (int(mon.month) == 4):
        month.append('April')
    elif (int(mon.month) == 5):
        month.append('May')
    elif (int(mon.month) == 6):
        month.append('June')
    elif (int(mon.month) == 7):
        month.append('July')
    elif (int(mon.month) == 8):
        month.append('August')
    elif (int(mon.month) == 9):
        month.append('September')
    elif (int(mon.month) == 10):
        month.append('October')
    elif (int(mon.month) == 11):
        month.append('November')
    elif (int(mon.month) == 12):
        month.append('December')
    df['Month'] = month
    hist = df['Month'].hist(bins=12)
    matplotlib.pyplot.show()


