def get_team_by_name(name, data):
    for team in data:
        if name == team['team_name']:
            return team