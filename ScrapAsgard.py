import requests
import bs4
import re

"""pages_epi_spe = ['https://www.stargate-fusion.com/sg1/personnages/81/ba-al.html','https://www.stargate-fusion.com/sg1/cultures/4/asgards.html','https://www.stargate-fusion.com/sg1/cultures/64/tok-ras.html','https://www.stargate-fusion.com/atlantis/personnages/738/todd.html']
for i in pages_epi_spe:
    response2 = requests.get(i)
    soup2 = bs4.BeautifulSoup(response2.text, 'html.parser')
    epi_spe = soup2.find_all("span", {"class":"liste_epi"})
    print(epi_spe) """

pages_episodes = ['https://www.stargate-fusion.com/sg1/episodes/9/109_le-marteau-de-thor.html',
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
'https://www.stargate-fusion.com/sg1/episodes/160/808_aux-yeux-du-monde.html',
'']
data = []
for page_episode in pages_episodes :
    ep = []
    response3 = requests.get(page_episode)
    soup3 = bs4.BeautifulSoup(response3.text, 'html.parser')
    info_epi = soup3.find_all("font")
    for epi in info_epi :
        ep.append(epi.next_sibling)
    data.append(ep)
print(data)

episodes = []
for d in data :    
    episode = {
        'titre' : d[0],
        'numero' : d[1],
        'audience_us' : d[3],
        'audience_fr' : d[4],
        'scenariste' : d[5],
        'realisateur' : d[6]
        }
    episodes.append(episode)
print(episodes)

