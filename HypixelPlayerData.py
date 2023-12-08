import requests
import json
import streamlit as st
import pandas as pd
import numpy as np
import sqlite3
import csv
import os
import io

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

##########################################
### BASE INFO - cards, employees, jobs ###
##########################################

def base_init_tables():
    conn, cursor = connect_to_db(base_db_path)
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS guild (
            g_name char(50) not null,
            g_uuid char(100) not null,
            g_members decimal(10,0) not null,
            g_level decimal(10,0) not null,
            g_creationdate date not null,
            g_tag char(10) not null
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS player (
            p_name char(50) not null,
            p_uuid char(100) not null,
            p_rank char(50) not null,
            p_joindate date not null,
            p_level decimal(10,0) not null
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pets(
            pt_name char(50) not null,
            pt_level decimal(10,0) not null,
            pt_owner char(100) not null
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS friends (
            f_player char(100) not null,
            f_friend char(100) not null
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS punishments (
        pu_player char(100) not null,
        pu_duration decimal(10,0) not null,
        pu_type char(50) not null
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS playergame(
            pl_player char(100) not null,
            pl_gameUUID char(100) not null
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS duels(
            d_gameUUID char(100) not null,
            d_coins decimal(10,0) not null,
            d_level decimal(10,0) not null,
            d_kills decimal(10,0) not null,
            d_deaths decimal(10,0) not null,
            d_wins decimal(10,0) not null,
            d_prestige decimal(10,0) not null
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS skywars(
            s_gameUUID char(100) not null,
            s_coins decimal(10,0) not null,
            s_level decimal(10,0) not null,
            s_kills decimal(10,0) not null,
            s_deaths decimal(10,0) not null,
            s_wins decimal(10,0) not null,
            s_prestige decimal(10,0) not null
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bedwars(
            b_gameUUID char(100) not null,
            b_coins decimal(10,0) not null,
            b_level decimal(10,0) not null,
            b_kills decimal(10,0) not null,
            b_deaths decimal(10,0) not null,
            b_wins decimal(10,0) not null,
            b_prestige decimal(10,0) not null
        )
    ''')


    
    commit_close(conn)



### BASE Info add to table
# def add_customer(groupName, quarantineFlag, facility_order, facility, quarantineHours, betweenCustomers):
#     conn, cursor = connect_to_db(base_db_path)
    
#     if quarantineFlag:
#         quarantineFlag = "True"
#     else:
#         quarantineFlag = "False"
#     cursor.execute('INSERT INTO cards (groupName, quarantineFlag, facility_order, facility, quarantineHours, betweenCustomers) VALUES (?, ?, ?, ?, ?, ?)',
#     (groupName, quarantineFlag, facility_order, facility, quarantineHours, betweenCustomers))
    
#     commit_close(conn)

# def add_employee(firstName, lastName):
#     conn, cursor = connect_to_db(base_db_path)
    
#     cursor.execute('INSERT OR IGNORE INTO employees (firstName, lastName) VALUES (?, ?)',
#     (firstName, lastName))
    
#     commit_close(conn)

# def add_job(grouping, site, subsite, facilityType, estDuration, Address):
#     conn, cursor = connect_to_db(base_db_path)
    
#     cursor.execute('INSERT OR IGNORE INTO jobs (grouping, site, subsite, facilityType, estDuration, Address) VALUES (?, ?, ?, ?, ?, ?)',
#     (grouping, site, subsite, facilityType, estDuration, Address))
    
#     commit_close(conn)



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
    url = "https://api.hypixel.net/player",
    params={
        "key": "5d69e9f7-5f3c-4e4b-b065-9e2a61e83c76",
        "uuid": uuid
    }
    ).json()

    


#website

st.title("Hypixel Player Data")
st.write("Enter a player's UUID to get their Hypixel stats")
uuid = st.text_input("UUID")


base_init_tables()
if uuid:
    st.write("Stats for: ", uuid)
    #check if player is in database
    if check_player(uuid):
        st.write("Player found in database")
    else:
        add_player(uuid)




    
    



