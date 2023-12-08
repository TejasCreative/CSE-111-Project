# FOR REQUESTING PLAYER DATA FROM HYPIXEL API

import requests as rq
from datetime import datetime, timezone, timedelta
import json

# Player Data needed

# note: we can't do friend or individual punishments (?)

## name
## uuid
## guild
## level
## rank
## join date

# Guild Data needed

## name
## uuid
## tag
## members
## level
## created

# Pet Data needed

## name
## level

# Game Data

## Duels

### type name: DUELS
### database name: Duels
### clean name: Duels

### coins
### level
### kills
### deaths
### wins
### losses (?)
### kd
### prestige

## Skywars

### type name: SKYWARS
### database name: SkyWars
### clean name: Skywars

### coins
### level
### kills
### deaths
### wins
### losses (?)
### kd
### prestige

## Bedwars

### type name: BEDWARS
### database name: Bedwars
### clean name: Bed Wars

### coins
### level
### kills
### deaths
### wins
### losses (?)
### kd
### prestige

# HIDE THIS LATER
# API Key

api_key = "5d69e9f7-5f3c-4e4b-b065-9e2a61e83c76"

# String UUID

uuid = "db8936f1e9b7472cb906c69d02f11222"

# ALL PLAYER DATA

data = rq.get(
    url = "https://api.hypixel.net/v2/player",
    params = {
        "key": api_key,
        "uuid": uuid
    }
).json()

with open("data.json", "w") as outfile:
    json.dump(data, outfile)

# PLAYER DATA

player_data = data["player"]

## name

name = player_data["displayname"]

## uuid

u_uuid = player_data["uuid"]

## guild

# guild = player_data["guild"]

## level

# level = player_data["level"]

## rank

# rank = player_data["packageRank"]

## join date

### time data is in unix epoch milliseconds

# function for conversion:

# def convert_epoch_to_pacific_time(epoch_time_ms):

#     epoch_time_seconds = epoch_time_ms / 1000.0

#     utc_datetime = datetime.utcfromtimestamp(epoch_time_seconds).replace(tzinfo=timezone.utc)

#     pacific_time = utc_datetime.astimezone(timezone(timedelta(hours=-8)))

#     return pacific_time

join_date = player_data["firstLogin"]

# with open('pdata.txt', 'w') as file:
#     print(data, file=file)

# file.close()

# data = rq.get(

#     url = "https://api.hypixel.net/player",
#     params = {
#         "key": api_key,
#         "uuid": uuid
#     }
# ).json()

# print(data)

# GAME DATA

## Duels

# DUELS DATA

duels_data = player_data["stats"]["Duels"]

    ### coins

duels_coins = duels_data["coins"]

    ### deaths

duels_deaths = duels_data["deaths"]

    ### games played

duels_games_played = duels_data["games_played_duels"]

    ### wins

duels_wins = duels_data["wins"]

    ### losses

duels_losses = duels_data["losses"]

    # SKYWARS DATA

skywars_data = player_data["stats"]["SkyWars"]

    ### coins

skywars_coins = skywars_data["coins"]

    ### deaths

skywars_deaths = skywars_data["deaths"]

    ### games played    

skywars_games_played = skywars_data["games_played_skywars"]

    ### wins

skywars_wins = skywars_data["wins"]

    ### losses

skywars_losses = skywars_data["losses"]

    # BEDWARS DATA

bedwars_data = player_data["stats"]["Bedwars"]

    ### coins

bedwars_coins = bedwars_data["coins"]

    ### deaths

bedwars_deaths = bedwars_data["deaths_bedwars"]

    ### games played

bedwars_games_played = bedwars_data["games_played_bedwars"]

    ### wins

bedwars_wins = bedwars_data["wins_bedwars"]
print(bedwars_wins)

    ### losses

bedwars_losses = bedwars_data["losses_bedwars"]
print(bedwars_losses)

### kd
### prestige

# GUILD

# guild_data = rq.get(
#     url = "https://api.hypixel.net/v2/guild",
#     params = {
#         "key": api_key,
#         "player": uuid
#     }
# ).json()

# with open("gdata.json", "w") as outfile:
#     json.dump(guild_data, outfile)


# print(guild_data)


# -------------------


# if using functions to access

# class PlayerData:
#     def __init__(self, uuid, api_key):
#         self.uuid = uuid
#         self.api_key = api_key
#         self.data = requests.get(
#             url = "https://api.hypixel.net/v2/player",
#             params={
#                 "key": self.api_key,
#                 "uuid": self.uuid
#             }
#         ).json()
    
#     def get_data(self):
#         return self.data
    
#     def get_username(self):
#         return self.data["player"]["displayname"]
    
#     def get_skywars_coins(self):
#         return self.data["player"]["stats"]["SkyWars"]["coins"]
    
#     def get_skywars_kills(self):
#         return self.data["player"]["stats"]["SkyWars"]["kills"]
    
#     def get_skywars_deaths(self):
#         return self.data["player"]["stats"]["SkyWars"]["deaths"]
    
#     def get_skywars_wins(self):
#         return self.data["player"]["stats"]["SkyWars"]["wins"]
    
#     def get_skywars_losses(self):
#         return self.data["player"]["stats"]["SkyWars"]["losses"]
    
#     def get_skywars_kd(self):
#         return self.get_skywars_kills() / self.get_skywars_deaths()
    
#     def get_skywars_wl(self):
#         return self.get_skywars_wins() / self.get_skywars_losses()
    
#     def get_skywars_kills_solo(self):
#         return self.data["player"]["stats"]["SkyWars"]["kills_solo"]
    
#     def get_skywars_deaths_solo(self):
#         return self.data["player"]["stats"]["SkyWars"]["deaths_solo"]
    
#     def get_skywars_wins_solo(self):
#         return self.data["player"]["stats"]["SkyWars"]["wins_solo"]
    
#     def get_skywars_losses_solo(self):
#         return self.data["player"]["stats"]["SkyWars"]["losses_solo"]
    
#     def get_skywars_kd_solo(self):
#         return self.get_skywars_kills_solo() / self.get_skywars_deaths_solo()
    
#     def get_skywars_wl_solo(self):
#         return self.get_skywars_wins_solo() / self.get_skywars_losses_solo()
    
#     def get_s