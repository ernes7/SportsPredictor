import requests
from bs4 import BeautifulSoup
from utils import get_team_by_name

url_form='https://thefishy.co.uk/formtable.php?table=1'
url_table="https://thefishy.co.uk/leaguetable.php?table=1&season=20"

def get_teams():
    data = []

    response_table = requests.get(url_table)
    response_form = requests.get(url_form)
    table_info = BeautifulSoup(response_table.text, 'html.parser')
    form_info = BeautifulSoup(response_form.text, 'html.parser')
    table = table_info.findAll('tr', attrs={"class":"cats2"})[1:21]
    form_home = form_info.find("div", {"id": "home"}).findAll('tr', attrs={"class":"cats2"})[1:21]
    form_away = form_info.find("div", {"id": "away"}).findAll('tr', attrs={"class":"cats2"})[1:21]

    for team in table:
        data.append({
            "id": None,
            "team_name": team.a.string,
            "form": [elem.string for elem in team.findAll('span', attrs={"class":"team-form"})][::-1],
            "top_players": [],
            "points": 0,
            "gd": team.findAll('td')[18].string,
            "ppg": float(team.findAll('td')[20].string),
            "games": team.findAll('td')[2].string
        })

    # Sort data by team name and assign Id
    data = sorted(data, key=lambda d: d['team_name']) 
    count = 1
    for team in data:
        team['id'] = count
        count += 1

    # Add next rival and locality and team form (home and away)
    for row in form_home:
        team = get_team_by_name(row.a.string, data)
        team['next_rival'] = row.findAll('a')[2].string[:-3].strip()
        team['locality'] = row.findAll('a')[2].string[-3:][1]
        team['form_home'] = [elem.string for elem in row.findAll('span', attrs={"class":"team-form"})][::-1]

    for row in form_away:
        team = get_team_by_name(row.a.string, data)
        team['form_away'] = [elem.string for elem in row.findAll('span', attrs={"class":"team-form"})][::-1]

    return data