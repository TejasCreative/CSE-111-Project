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
    cursor.execute('SELECT * FROM guild WHERE g_uuid = ?', (uuid,))
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
        "key": "5d69e9f7-5f3c-4e4b-b065-9e2a61e83c76",
        "player": uuid
    }
    ).json()

    if(data["success"] == False):
        st.write("Player not in guild")
        st.stop()
    player_data = data["guild"]
    name = player_data["name"]
    id = player_data["_id"]
    tag = player_data["tag"]
    created = epoche_to_date(player_data["created"])
    level = player_data["exp"]
    members = ""
    for i in range(len(player_data["members"])):
        members += player_data["members"][i]["uuid"] + ","
        if(i>50):
            break
        




        

    conn, cursor = connect_to_db(base_db_path)
    cursor.execute('INSERT INTO guild VALUES (?, ?, ?, ?, ?, ?)', (name, id, members, level, created, tag))
    commit_close(conn)






#read and display player data
def read_player(uuid):
    conn, cursor = connect_to_db(base_db_path)
    cursor.execute('SELECT * FROM guild WHERE g_uuid = ?', (uuid,))
    rows = cursor.fetchall()

    

    st.write("Guild Name: ", rows[0][0])
    st.write("Guild ID: ", rows[0][1])
    st.write("Guild Members: ", rows[0][2])
    st.write("Guild Level: ", rows[0][3])
    st.write("Guild Created: ", rows[0][4])
    st.write("Guild Tag: ", rows[0][5])
    



    

    commit_close(conn)






#def get guild name from API
def get_guild_name(uuid):
    data = requests.get(
    url = "https://api.hypixel.net/v2/guild",
    params={
        "key": "5d69e9f7-5f3c-4e4b-b065-9e2a61e83c76",
        "player": uuid
    }
    ).json()

    if(data["success"] == False):
        st.write("Player not in guild")
        st.stop()
    player_data = data["guild"]
    name = player_data["_id"]
    return name



#website


st.title("Hypixel Guild Data")
st.write("Enter a players ID to get the guild data for that guild")
guild = st.text_input("Player Name: ")


if guild:
    st.write("Stats for: ", guild)
    #check if player is in database
    name = get_guild_name(guild)
    
    if (check_player(name) == False):
        add_player(name)
    
    read_player(name)
    



    

    

    

    

    