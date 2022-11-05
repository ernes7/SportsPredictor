from utils import get_team_by_name

def calculate_points_for_team(team, data):
    points=0
    
    if team['locality'] == 'h':
        # 1 point for locality
        points += 1
        # HOME FORM if home
        for game in team['form_home'][:3]:
            if game.lower() == 'w':
                points += 2
            if game.lower() == 'd':
                points += 1
    else:
        # AWAY FORM if away
        for game in team['form_away'][:3]:
            if game.lower() == 'w':
                points += 2
            if game.lower() == 'd':
                points += 1
    
    # GENERAL FORM last 5 games
    for game in team['form'][:5]:
        if game.lower() == 'w':
            points += 2
        if game.lower() == 'd':
            points += 1

    # check if player chance_of_playing_next_round < 90
    # for player in team['top_players']:
    #     if player['chance_of_playing_next_round'] is not None and player['chance_of_playing_next_round'] < 90:
    #         points -= 1

    # PPG difference x3 
    rival = get_team_by_name(team['next_rival'], data)
    points += abs(team['ppg']-rival['ppg'])*3

    team['points'] = points