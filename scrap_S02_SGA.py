import requests
import bs4
import re


pages_episodes_S02_SGA = [
    'https://www.stargate-fusion.com/atlantis/episodes/262/301_menace-sur-la-terre.html',
    'https://www.stargate-fusion.com/atlantis/episodes/263/302_transformation.html',
    'https://www.stargate-fusion.com/atlantis/episodes/265/303_irresistible.html',
    'https://www.stargate-fusion.com/atlantis/episodes/264/304_face-a-face.html',
    'https://www.stargate-fusion.com/atlantis/episodes/266/305_copies-conformes.html',
    'https://www.stargate-fusion.com/atlantis/episodes/280/306_le-monde-reel.html',
    'https://www.stargate-fusion.com/atlantis/episodes/281/307_interets-communs.html',
    'https://www.stargate-fusion.com/atlantis/episodes/282/308_la-guerre-des-genies.html',
    'https://www.stargate-fusion.com/atlantis/episodes/283/309_la-machine-infernale.html',
    'https://www.stargate-fusion.com/atlantis/episodes/284/310_exil-force-1-2.html',
    'https://www.stargate-fusion.com/atlantis/episodes/285/311_exil-force-2-2.html',
    'https://www.stargate-fusion.com/atlantis/episodes/288/312_le-chant-des-baleines.html',
    'https://www.stargate-fusion.com/atlantis/episodes/286/313_invincible.html',
    'https://www.stargate-fusion.com/atlantis/episodes/289/314_le-peril-de-la-sagesse.html'
    'https://www.stargate-fusion.com/atlantis/episodes/290/315_les-jeux-sont-faits.html',
    'https://www.stargate-fusion.com/atlantis/episodes/291/316_ames-en-detresse.html',
    'https://www.stargate-fusion.com/atlantis/episodes/287/317_une-question-d-ethique.html',
    'https://www.stargate-fusion.com/atlantis/episodes/292/318_immersion.html',
    'https://www.stargate-fusion.com/atlantis/episodes/293/319_l-equilibre-parfait.html',
    'https://www.stargate-fusion.com/atlantis/episodes/294/320_nom-de-code-horizon.html']
data_S02_SGA = []
for page_episode_S02_SGA in pages_episodes_S02_SGA :
    ep_S02_SGA = []
    response_S02_SGA = requests.get(page_episode_S02_SGA)
    soup_S02_SGA = bs4.BeautifulSoup(response_S02_SGA.text, 'html.parser')
    info_epi_S02_SGA = soup_S02_SGA.find_all("font")
    for epi_S02_SGA in info_epi_S02_SGA :
        ep_S02_SGA.append(epi_S02_SGA.next_sibling)
    data_S02_SGA.append(ep_S02_SGA)
#print(data_S02_SGA)

episodes_S02_SGA = []
for d_S02_SGA in data_S02_SGA :    
    episode_S02_SGA = {
        'titre' : d_S02_SGA[0],
        'numero' : d_S02_SGA[1],
        'date de diffusion' : d_S02_SGA[2],
        'audience_us' : d_S02_SGA[3],
        'audience_fr' : d_S02_SGA[4],
        'scenariste' : d_S02_SGA[5],
        'realisateur' : d_S02_SGA[6]
        }
    episodes_S02_SGA.append(episode_S02_SGA)
print(episodes_S02_SGA)
