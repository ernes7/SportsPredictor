import requests

url_fantasy='https://fantasy.premierleague.com/api/bootstrap-static/'
fantasy = requests.get(url_fantasy).json()


def team_retriever_by_id(id, data):
    for team in data:
        if id == team['id']:
            return team

# Loop through fantasy elements, if player team = team id and player points>20, add to top_players of team
def get_top_players(data):
    for player in fantasy['elements']:
        if player['total_points'] > 20:
            team_retriever_by_id(player['team'], data)['top_players'].append(player)

    # Shrink top players to 5, sorted by total points
    for team in data:
        team['top_players'] = sorted(team['top_players'], key=lambda d: d['total_points'], reverse=True)[:5]