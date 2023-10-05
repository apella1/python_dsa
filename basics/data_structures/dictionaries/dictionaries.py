"""Python built in dict"""
teams = {}
teams["laliga"] = "real"
teams["epl"] = "city"
teams["serieA"] = "lecce"

print(teams.keys())
print(teams.values())
# Returns a list of tuple of the key-value pairs
print(teams.items())

for league, team in teams.items():
    print(team, "->", league)
