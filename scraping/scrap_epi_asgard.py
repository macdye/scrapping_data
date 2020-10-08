import requests
import bs4
import re

pages_episodes_asgard = [
    'https://www.stargate-fusion.com/sg1/episodes/9/109_le-marteau-de-thor.html',
    'https://www.stargate-fusion.com/sg1/episodes/27/206_l-oeil-de-pierre.html',
    'https://www.stargate-fusion.com/sg1/episodes/36/215_la-cinquieme-race.html',
    'https://www.stargate-fusion.com/sg1/episodes/46/303_diplomatie.html',
    'https://www.stargate-fusion.com/sg1/episodes/61/318_trahisons.html',
    'https://www.stargate-fusion.com/sg1/episodes/65/322_nemesis.html',
    'https://www.stargate-fusion.com/sg1/episodes/66/401_victoires-illusoires.html',
    'https://www.stargate-fusion.com/sg1/episodes/92/505_mission-soleil-rouge.html',
    'https://www.stargate-fusion.com/sg1/episodes/104/517_impact.html',
    'https://www.stargate-fusion.com/sg1/episodes/109/522_revelations.html',
    'https://www.stargate-fusion.com/sg1/episodes/112/603_reunion.html',
    'https://www.stargate-fusion.com/sg1/episodes/120/611_promethee.html',
    'https://www.stargate-fusion.com/sg1/episodes/121/612_evolution.html',
    'https://www.stargate-fusion.com/sg1/episodes/126/617_secret-d-etat.html',
    'https://www.stargate-fusion.com/sg1/episodes/134/703_l-apprenti-sorcier.html',
    'https://www.stargate-fusion.com/sg1/episodes/154/801_mesalliance-1-2.html',
    'https://www.stargate-fusion.com/sg1/episodes/155/802_mesalliance-2-2.html',
    'https://www.stargate-fusion.com/sg1/episodes/160/808_aux-yeux-du-monde.html']
data_asgard = []
for page_episode_asgard in pages_episodes_asgard :
    ep_asgard = []
    response_asgard = requests.get(page_episode_asgard)
    soup_asgard = bs4.BeautifulSoup(response_asgard.text, 'html.parser')
    info_epi_asgard = soup_asgard.find_all("font")
    for epi_asgard in info_epi_asgard :
        ep_asgard.append(epi_asgard.next_sibling)
    data_asgard.append(ep_asgard)
#print(data_asgard)

episodes_asgard = []
for d_asgard in data_asgard :
    episode_asgard = {
        'title': d_asgard[0],
        'epi_num': d_asgard[1],
        'diffusion_date': d_asgard[2],
        'audience_us' : d_asgard[3],
        'audience_fr' : d_asgard[4],
        'scenarist' : d_asgard[5],
        'director': d_asgard[6]
        }
    episodes_asgard.append(episode_asgard)
#print(episodes_asgard)

