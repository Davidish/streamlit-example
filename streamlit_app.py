import datetime
import streamlit as st
import pandas as pd
from os.path import exists
import pathlib

file_exists = exists(pathlib.Path('data.parquet'))
st.title("Harry's Timesheet App")

t1 = st.time_input('Start time:', datetime.time(8, 00))
t2 = st.time_input('End time:', datetime.time(8, 00))
user = 'system'
insert_datetime = datetime.datetime.now()

if st.button('Submit'):
    if file_exists:
        df = pd.read_parquet('data.parquet')
        details = {
            'start_time' : [t1],
            'end_time' : [t2],
            'user' : [user],
            'insert_datetime':[insert_datetime]
        }
        df_insert = pd.DataFrame(details)
        df = pd.concat([df, df_insert], ignore_index=True, sort=False)        
    else:
        details = {
            'start_time' : [t1],
            'end_time' : [t2],
            'user' : [user],
            'insert_datetime':[insert_datetime]
        }
        df = pd.DataFrame(details)
        
    df.to_parquet('data.parquet')
    st.write('Entry submitted...')
    st.dataframe(df)
