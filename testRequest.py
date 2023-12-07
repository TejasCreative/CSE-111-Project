import requests
import pandas as pd
import json

# using my api key and my uuid

data = requests.get(
    url = "https://api.hypixel.net/player",
    params={
        "key": "22dcff9c-34e5-4376-a2dc-58c3e4d23ebe",
        "uuid": "db8936f1e9b7472cb906c69d02f11222"
    }
).json()

# ALL the player data for the player is now in "data"
# We can add the data to our own database so that we don't have to request that much data over and over

# example: retrieving skywars coins

skywars_coins = data["player"]["stats"]["SkyWars"]["coins"]

print(skywars_coins)

