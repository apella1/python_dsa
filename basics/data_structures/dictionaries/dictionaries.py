"""Python built in dict"""
teams = {}
teams["laliga"] = "real"
teams["epl"] = "city"
teams["serieA"] = "lecce"

print(teams.keys())
print(teams.values())
print(teams.items())

for league, team in teams.items():
    print(team, "->", league)
