def game_dict():
    return {
        "home": {
            "team_name": "Cleveland Cavaliers",
            "colors": ["wine", "gold"],
            "players": {
                "Lebron James": {
                    "number": 23,
                    "position": "forward",
                    "points_per_game": 27.0,
                    "rebounds_per_game": 8.0,
                    "assists_per_game": 9.0
                },
                "Kevin Love": {
                    "number": 0,
                    "position": "center",
                    "points_per_game": 17.0,
                    "rebounds_per_game": 10.0,
                    "assists_per_game": 2.0
                }
            }
        },
        "away": {
            "team_name": "Golden State Warriors",
            "colors": ["blue", "yellow"],
            "players": {
                "Stephen Curry": {
                    "number": 30,
                    "position": "guard",
                    "points_per_game": 30.0,
                    "rebounds_per_game": 5.0,
                    "assists_per_game": 6.0
                },
                "Klay Thompson": {
                    "number": 11,
                    "position": "guard",
                    "points_per_game": 20.0,
                    "rebounds_per_game": 3.0,
                    "assists_per_game": 2.0
                }
            }
        }
    }

def num_points_per_game(player_name):
    game_data = game_dict()
    for team in game_data.values():
        for player, stats in team["players"].items():
            if player == player_name:
                return stats["points_per_game"]
    return None

def player_age(player_name):
    game_data = game_dict()
    for team in game_data.values():
        for player, stats in team["players"].items():
            if player == player_name:
                return stats["age"]
    return None

def team_colors(team_name):
    game_data = game_dict()
    for team in game_data.values():
        if team["team_name"] == team_name:
            return team["colors"]
    return None

def team_names():
    game_data = game_dict()
    return [team["team_name"] for team in game_data.values()]

def player_numbers(team_name):
    game_data = game_dict()
    for team in game_data.values():
        if team["team_name"] == team_name:
            return [player["number"] for player in team["players"].values()]
    return None

def player_stats(player_name):
    game_data = game_dict()
    for team in game_data.values():
        for player, stats in team["players"].items():
            if player == player_name:
                return stats
    return None

def average_rebounds_by_shoe_brand():
    game_data = game_dict()
    shoe_brands = {}
    for team in game_data.values():
        for player, stats in team["players"].items():
            shoe_brand = stats.get("shoe_brand")
            rebounds = stats.get("rebounds_per_game")
            if shoe_brand and rebounds:
                if shoe_brand not in shoe_brands:
                    shoe_brands[shoe_brand] = []
                shoe_brands[shoe_brand].append(rebounds)
   
    for brand, rebounds_list in shoe_brands.items():
        average_rebounds = sum(rebounds_list) / len(rebounds_list)
        print(f"{brand}: {average_rebounds:.2f}")