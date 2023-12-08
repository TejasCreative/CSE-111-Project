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
        st.write("No Punishments Found for Player: ", uuid)
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
    cursor.execute('SELECT * FROM pets WHERE pt_owner = ?', (uuid,))
    rows = cursor.fetchall()

    

    st.write("Pets: ")
    st.write("Red Panda Level 50")


        
    



    

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
        st.write("No Pets Found for Player: ", uuid)
        st.stop()
    player_data = data["guild"]
    name = player_data["_id"]
    return name



#website


st.title("Hypixel Pet Data")
st.write("Enter a players ID to get their Pets")
guild = st.text_input("Player Name: ")


if guild:
    st.write("Stats for: ", guild)
    #check if player is in database



    
    read_player(guild)
    



    

    

    

    

    