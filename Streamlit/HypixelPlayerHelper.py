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

playerCount = 0

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
    global playerCount
    playerCount = playerCount+1

    data = requests.get(
    url = "https://api.hypixel.net/player",
    params={
        "key": "5d69e9f7-5f3c-4e4b-b065-9e2a61e83c76",
        "uuid": uuid
    }
    ).json()

    player_data = data["player"]
    name = player_data["displayname"]
    u_uuid = player_data["uuid"]
    join_date = epoche_to_date(player_data["firstLogin"])
    rank = player_data["newPackageRank"]
    level = player_data["networkExp"]

    conn, cursor = connect_to_db(base_db_path)
    cursor.execute('INSERT INTO player VALUES (?, ?, ?, ?, ?)', (name, u_uuid, rank, join_date, level))
    commit_close(conn)
    add_duels(uuid)
    add_skywars(uuid)
    add_bedwars(uuid)


def add_duels(uuid):
    data = requests.get(
    url = "https://api.hypixel.net/player",
    params={
        "key": "5d69e9f7-5f3c-4e4b-b065-9e2a61e83c76",
        "uuid": uuid
    }
    ).json()

    player_data = data["player"]

    # DUELS UUID

    duels_uuid = playerCount

    # DUELS DATA

    duels_data = player_data["stats"]["Duels"]

    ### coins

    duels_coins = duels_data["coins"]

    ### level

    duels_level = duels_data["wins"]
    duels_level = duels_level/10
    
    ### kills

    duels_kills = duels_data["wins"]

    ### deaths

    duels_deaths = duels_data["deaths"]

    ### games played

    duels_games_played = duels_data["games_played_duels"]

    ### wins

    duels_wins = duels_data["wins"]


    ### prestige

    duels_prestige = duels_data["wins"]
    duels_prestige = duels_prestige/50

    conn, cursor = connect_to_db(base_db_path)
    cursor.execute('INSERT INTO duels VALUES (?, ?, ?, ?, ?, ?, ?)', (duels_uuid, duels_coins, duels_level, duels_kills, duels_deaths, duels_wins, duels_prestige))
    cursor.execute('INSERT INTO playergame VALUES (?, ?)', (uuid, duels_uuid))
    commit_close(conn)

def add_skywars(uuid):

    data = requests.get(
    url = "https://api.hypixel.net/v2/player",
    params={
        "key": "5d69e9f7-5f3c-4e4b-b065-9e2a61e83c76",
        "uuid": uuid
    }
    ).json()

    player_data = data["player"]

    # SKYWARS DATA

    skywars_uuid = playerCount

    skywars_data = player_data["stats"]["SkyWars"]

    ### coins

    skywars_coins = skywars_data["coins"]

    ### level

    skywars_level = skywars_data["skywars_experience"]

    ### kills

    skywars_kills = skywars_data["kills"]

    ### deaths

    skywars_deaths = skywars_data["deaths"]

    ### wins

    skywars_wins = skywars_data["wins"]

    ### prestige

    skywars_prestige = skywars_level/100

    conn, cursor = connect_to_db(base_db_path)
    cursor.execute('INSERT INTO skywars VALUES (?, ?, ?, ?, ?, ?, ?)', (skywars_uuid, skywars_coins, skywars_level, skywars_kills, skywars_deaths, skywars_wins, skywars_prestige))
    cursor.execute('INSERT INTO playergame VALUES (?, ?)', (uuid, skywars_uuid))
    commit_close(conn)


def add_bedwars(uuid):
    
        data = requests.get(
        url = "https://api.hypixel.net/v2/player",
        params={
            "key": "5d69e9f7-5f3c-4e4b-b065-9e2a61e83c76",
            "uuid": uuid
        }
        ).json()
    
        player_data = data["player"]
    
        # BEDWARS DATA
    
        bedwars_uuid = playerCount
    
        bedwars_data = player_data["stats"]["Bedwars"]
    
        ### coins
    
        bedwars_coins = bedwars_data["coins"]
    
        ### level
    
        bedwars_level = bedwars_data["Experience"]
    
        ### kills
    
        bedwars_kills = bedwars_data["kills_bedwars"]
    
        ### deaths
    
        bedwars_deaths = bedwars_data["deaths_bedwars"]
    
        ### wins
    
        bedwars_wins = bedwars_data["wins_bedwars"]
    
        ### prestige
    
        bedwars_prestige = bedwars_level/100
    
        conn, cursor = connect_to_db(base_db_path)
        cursor.execute('INSERT INTO bedwars VALUES (?, ?, ?, ?, ?, ?, ?)', (bedwars_uuid, bedwars_coins, bedwars_level, bedwars_kills, bedwars_deaths, bedwars_wins, bedwars_prestige))
        cursor.execute('INSERT INTO playergame VALUES (?, ?)', (uuid, bedwars_uuid))
        commit_close(conn)
    




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

    # #get corresponding game data
    # cursor.execute('SELECT * FROM playergame WHERE pl_player = ?', (uuid,))
    # rows = cursor.fetchall()
    # uid = rows[0][1]
    # st.write("Player Game uid: ", uid)

    cursor.execute('SELECT * FROM duels WHERE d_gameUUID = ? JOIN playergame, (uid,))



    st.write("SkyWars Stats: ")
    cursor.execute('SELECT * FROM skywars WHERE s_gameUUID = ?', join , (uid,))
    rows = cursor.fetchall()
    st.write("Coins: ", rows[0][1])
    st.write("Level: ", rows[0][2])
    st.write("Kills: ", rows[0][3])
    st.write("Deaths: ", rows[0][4])
    st.write("Wins: ", rows[0][5])


    st.write("Bedwars Stats: ")
    cursor.execute('SELECT * FROM bedwars WHERE b_gameUUID = ?', (uid,))
    rows = cursor.fetchall()
    st.write("Coins: ", rows[0][1])
    st.write("Level: ", rows[0][2])
    st.write("Kills: ", rows[0][3])
    st.write("Deaths: ", rows[0][4])
    st.write("Wins: ", rows[0][5])

    st.write("Duels Stats: ")
    cursor.execute('SELECT * FROM duels WHERE d_gameUUID = ?', (uid,))
    rows = cursor.fetchall()
    st.write("Coins: ", rows[0][1])
    st.write("Level: ", rows[0][2])
    st.write("Kills: ", rows[0][3])
    st.write("Deaths: ", rows[0][4])
    st.write("Wins: ", rows[0][5])

    



    commit_close(conn)









#website

st.title("Hypixel Player Helper")
st.write("Enter a player's UUID to get their Hypixel stats")
uuid = st.text_input("UUID")


base_init_tables()
if uuid:
    st.write("Stats for: ", uuid)
    #check if player is in database
    if (check_player(uuid) == False):
        add_player(uuid)

    read_player(uuid)
    



    

    

    

