from Apis.fantasy_pl import get_top_players
from WebScrap.teams_pl import get_teams
from calculate import calculate_points_for_team

url_predictions='https://www.rotowire.com/soccer/lineups.php'

def main():
    data = get_teams()
    get_top_players(data)   
    for team in data:
        calculate_points_for_team(team)


    for team in data:
        print(team['team_name'], team['points'])