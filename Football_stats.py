import requests
from bs4 import BeautifulSoup

# URL for CBS NFL Stats
url = "https://www.cbssports.com/nfl/stats/playersort/nfl/year-2021-season-regular-category-touchdowns"

# Send a request to the website
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table with player statistics
table = soup.find('table', class_='TableBase-table')

# Extract the top 20 players
players = table.find_all('tr')[1:21]

print("{:<25} {:<20} {:<10} {:<15}".format('Player', 'Position', 'Team', 'Touchdowns'))
for player in players:
    stats = player.find_all('td')
    name = stats[0].text.strip()
    position = stats[1].text.strip()
    team = stats[2].text.strip()
    touchdowns = stats[3].text.strip()
    print("{:<25} {:<20} {:<10} {:<15}".format(name, position, team, touchdowns))
