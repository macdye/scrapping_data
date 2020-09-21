import requests
import bs4
import re

pages_episodes_todd = [
    'https://www.stargate-fusion.com/atlantis/episodes/281/307_interets-communs.html',
    'https://www.stargate-fusion.com/atlantis/episodes/305/408_le-prophete.html',
    'https://www.stargate-fusion.com/atlantis/episodes/309/409_programmation-mortelle.html',
    'https://www.stargate-fusion.com/atlantis/episodes/311/411_alliance-forcee.html',
    'https://www.stargate-fusion.com/atlantis/episodes/312/412_consequences.html',
    'https://www.stargate-fusion.com/atlantis/episodes/314/417_infiltration-wraith.html',
    'https://www.stargate-fusion.com/atlantis/episodes/320/418_hybrides-1-2.html',
    'https://www.stargate-fusion.com/atlantis/episodes/323/420_le-dernier-homme.html',
    'https://www.stargate-fusion.com/atlantis/episodes/332/508_la-nouvelle-reine.html',
    'https://www.stargate-fusion.com/atlantis/episodes/334/510_premier-contact-1-2.html',
    'https://www.stargate-fusion.com/atlantis/episodes/341/517_entre-la-vie-et-la-mort.html',
    'https://www.stargate-fusion.com/atlantis/episodes/344/520_l-empire-contre-attaque.html']
data_todd = []
for page_episode_todd in pages_episodes_todd :
    ep_todd = []
    response_todd = requests.get(page_episode_todd)
    soup_todd = bs4.BeautifulSoup(response_todd.text, 'html.parser')
    info_epi_todd = soup_todd.find_all("font")
    for epi_todd in info_epi_todd :
        ep_todd.append(epi_todd.next_sibling)
    data_todd.append(ep_todd)
#print(data_todd)

episodes_todd = []
for d_todd in data_todd :    
    episode_todd = {
        'titre' : d_todd[0],
        'numero' : d_todd[1],
        'date de diffusion' : d_todd[2],
        'audience_us' : d_todd[3],
        'audience_fr' : d_todd[4],
        'scenariste' : d_todd[5],
        'realisateur' : d_todd[6]
        }
    episodes_todd.append(episode_todd)
print(episodes_todd)