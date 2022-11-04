import requests
from bs4 import BeautifulSoup
url_team='https://thefishy.co.uk/formtable.php?table=1'

def get_teams():
    data = []

    response_teams = requests.get(url_team)
    team_info = BeautifulSoup(response_teams.text, 'html.parser')
    teams = team_info.findAll('tr', attrs={"class":"cats2"})[1:21]

    for title in teams:
        data.append({
            "id": None,
            "team_name": title.a.string,
            "form": [elem.string for elem in title.findAll('span', attrs={"class":"team-form"})][::-1],
            "next_rival": title.findAll('a')[2].string[:-3].strip(),
            "top_players": [],
            "locality": title.findAll('a')[2].string[-3:][1],
            "points": 0,
        })

    # Sort data by team name and assign Id
    data = sorted(data, key=lambda d: d['team_name']) 
    count = 1
    for team in data:
        team['id'] = count
        count += 1


    return data