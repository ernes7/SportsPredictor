from Apis.fantasy_pl import get_top_players
from WebScrap.teams_pl import get_teams
from calculate import calculate_points_for_team
from utils import get_team_by_name

def main():
    data = get_teams()
    get_top_players(data)   
    for team in data:
        calculate_points_for_team(team, data)

    for team in data:
        print(team['team_name'], team['points'])
        rival = get_team_by_name(team['next_rival'], data)
        print(rival['team_name'], rival['points'])
        print("-------------------------------\n")

if __name__ == "__main__":
    main()