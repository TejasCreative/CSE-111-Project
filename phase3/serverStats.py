# GENERAL SERVER STATS

import requests as rq

api_key = ""

# BOOSTERS

# time is in unix epoch milliseconds

# expected:
# {
#   "success": true,
#   "boosters": [
#     {
#       "_id": "string",
#       "purchaserUuid": "ad8fefaa8351454bb739a4eaa872173f",
#       "amount": 0,
#       "originalLength": 0,
#       "length": 0,
#       "gameType": 0,
#       "dateActivated": 0,
#       "stacked": [
#         "ad8fefaa-8351-454b-b739-a4eaa872173f"
#       ]
#     }
#   ],
#   "boosterState": {
#     "decrementing": true
#   }
# }

boosters = rq.get(
    url = "https://api.hypixel.net/v2/boosters",
    params={
        "key": api_key
    }
).json()

print(boosters)

# PLAYER COUNT

# expected:

# {
#   "success": true,
#   "playerCount": 0,
#   "games": {
#     "GAME_TYPE": {
#       "players": 2,
#       "modes": {
#         "mode_1": 1,
#         "mode_2": 1
#       }
#     }
#   }
# }

player_count = rq.get(
    url="https://api.hypixel.net/v2/counts",
    params={
        "key": api_key
    }
).json()

print(player_count)

# LEADERBOARDS

# expected:

# {
#   "success": true,
#   "leaderboards": {}
# }

leaderboards = rq.get(
    url="https://api.hypixel.net/v2/leaderboards",
    params={
        "key": api_key
    }
).json()

# skywars leaderboard

skywars_leaderboard = leaderboards["leaderboards"]["SKYWARS"]

duels_leaderboard = leaderboards["leaderboards"]["DUELS"]

bedwars_leaderboard = leaderboards["leaderboards"]["BEDWARS"]

# print(skywars_leaderboard)