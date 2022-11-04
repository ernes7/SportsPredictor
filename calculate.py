def calculate_points_for_team(team):
    points=0
    if team['locality'] == 'h':
        points += 1
    
    for game in team['form'][:5]:
        if game.lower() == 'w':
            points += 2
        if game.lower() == 'd':
            points += 1

    for game in team['form'][:5]:
        if team['locality'] == 'h':
            if game == 'W':
                points += 2
            if game == 'D':
                points += 1

    # check if player chance_of_playing_next_round == 100
    # for player in team['top_players']:
    #     if player['chance_of_playing_next_round'] is not None and player['chance_of_playing_next_round'] > 90:
    #         points += 1

    # PPG difference x3 

    # 

    team['points'] = points