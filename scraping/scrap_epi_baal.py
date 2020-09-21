import requests
import bs4
import re

pages_episodes_baal = [
    'https://www.stargate-fusion.com/sg1/episodes/102/515_sans-issue-1-2.html',
    'https://www.stargate-fusion.com/sg1/episodes/103/516_sans-issue-2-2.html',
    'https://www.stargate-fusion.com/sg1/episodes/115/606_abysse.html',
    'https://www.stargate-fusion.com/sg1/episodes/133/702_retour-aux-sources-2-2.html',
    'https://www.stargate-fusion.com/sg1/episodes/157/804_heure-h.html',
    'https://www.stargate-fusion.com/sg1/episodes/203/816_la-derniere-chance-1-2.html',
    'https://www.stargate-fusion.com/sg1/episodes/204/817_la-derniere-chance-2-2.html',
    'https://www.stargate-fusion.com/sg1/episodes/205/818_pour-la-vie.html',
    'https://www.stargate-fusion.com/sg1/episodes/233/907_terre-d-asile.html',
    'https://www.stargate-fusion.com/sg1/episodes/275/1010_la-quete-du-graal-1-2.html',
    'https://www.stargate-fusion.com/sg1/episodes/276/1011_la-quete-du-graal-2-2.html',
    'https://www.stargate-fusion.com/sg1/episodes/299/1019_la-symbiose-du-mal.html',
    'https://www.stargate-fusion.com/sg1/telefilms/316/2_continuum.html']
data_baal = []
for page_episode_baal in pages_episodes_baal :
    ep_baal = []
    response_baal = requests.get(page_episode_baal)
    soup_baal = bs4.BeautifulSoup(response_baal.text, 'html.parser')
    info_epi_baal = soup_baal.find_all("font")
    for epi_baal in info_epi_baal :
        ep_baal.append(epi_baal.next_sibling)
    data_baal.append(ep_baal)
#print(data_baal)

episodes_baal = []
for d_baal in data_baal :    
    episode_baal = {
        'titre' : d_baal[0],
        'numero' : d_baal[1],
        'date de diffusion' : d_baal[2],
        'audience_us' : d_baal[3],
        'audience_fr' : d_baal[4],
        'scenariste' : d_baal[5],
        'realisateur' : d_baal[6]
        }
    episodes_baal.append(episode_baal)
print(episodes_baal)