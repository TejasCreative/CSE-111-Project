import requests
import pandas as pd
import json

# using my api key and my uuid

data = requests.get(
    url = "https://api.hypixel.net/player",
    params={
        "key": "5d69e9f7-5f3c-4e4b-b065-9e2a61e83c76",
        "uuid": "7eba395815364e18aac5d6b4d12bbc08"
    }
).json()

# ALL the player data for the player is now in "data"
# We can add the data to our own database so that we don't have to request that much data over and over

# example: retrieving skywars coins

# skywars_coins = data["player"]["stats"]["SkyWars"]["coins"]

# print(skywars_coins)

print(type(data))

skywars_coins = data["player"]["stats"]["SkyWars"]["coins"]
print(skywars_coins)
