import requests
import json
import streamlit as st
import pandas as pd
import numpy as np
import sqlite3
import csv
import os
import io
import datetime
from datetime import datetime as dt

# Function to get player data
db_path = '/Users/tejas/Desktop/CSE-111-Project/data.db'
base_db_path = '/Users/tejas/Desktop/CSE-111-Project/data.db'
def connect_to_db(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    return conn, cursor

def commit_close(conn):
    conn.commit()
    conn.close()



#epoche time to date
def epoche_to_date(epoche):
    return dt.fromtimestamp(epoche/1000).strftime('%Y-%m-%d %H:%M:%S')


#check if player is in database
def check_player(uuid):
    conn, cursor = connect_to_db(base_db_path)
    cursor.execute('SELECT * FROM player WHERE p_uuid = ?', (uuid,))
    rows = cursor.fetchall()
    if len(rows) == 0:
        return False
    else:
        return True

#use API to get player data
def add_player(uuid):
    data = requests.get(
    url = "https://api.hypixel.net/v2/guild",
    params={
        "name": uuid
    }
    ).json()
    st.write(data)

    




#read and display player data
def read_player(uuid):
    conn, cursor = connect_to_db(base_db_path)
    cursor.execute('SELECT * FROM player WHERE p_uuid = ?', (uuid,))
    rows = cursor.fetchall()



    st.write("Player Name: ", rows[0][0])
    st.write("Player UUID: ", rows[0][1])
    st.write("Player Rank: ", rows[0][2])
    st.write("Player Join Date: ", rows[0][3])
    st.write("Player Level: ", rows[0][4])

    commit_close(conn)









#website

st.title("Hypixel Guild Data")
st.write("Enter a guild name to get stats for that guild")
guild = st.text_input("Guild Name: ")


if guild:
    st.write("Stats for: ", guild)
    #check if player is in database
    if (check_player(guild) == False):
        add_player(guild)
    read_player(guild)
    



    

    

    

    

    