import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 


def cleaning(csv):
    # read in data
    df = pd.read_csv(f'../data/{csv}')
    # dropping columns and filling in missing values
    df.dropna(subset=['precip'], inplace=True)
    df.drop(columns=['snow', 'snowdepth', 'severerisk'], inplace=True)
    mean = df['winddir'].mean()
    df['winddir'] = df['winddir'].fillna(mean)
    col_drop = [i for i in df.columns if df[i].isnull().sum() > (len(df) / 2)]
    df.drop(columns = col_drop, inplace = True)
    # dummifying 'icon' column
    df[['clear-day', 'cloudy', 'fog', 'partly-cloudy-day', 'rain_icon', 'wind']] = pd.get_dummies(df['icon'], dtype='int')
    # converting 'datetime' column to index
    df['datetime'] = pd.to_datetime(df['datetime'])
    df.set_index('datetime', inplace=True)
    df.sort_index(inplace=True)
    # saving csv file
    df.to_csv(f'../data/{csv[:-6]}.csv', index_label='datetime')