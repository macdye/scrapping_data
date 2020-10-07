import requests
import bs4
import re

pages_episodes_S03_SGA = [
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
    'https://www.stargate-fusion.com/atlantis/episodes/289/314_le-peril-de-la-sagesse.html',
    'https://www.stargate-fusion.com/atlantis/episodes/290/315_les-jeux-sont-faits.html',
    'https://www.stargate-fusion.com/atlantis/episodes/291/316_ames-en-detresse.html',
    'https://www.stargate-fusion.com/atlantis/episodes/287/317_une-question-d-ethique.html',
    'https://www.stargate-fusion.com/atlantis/episodes/292/318_immersion.html',
    'https://www.stargate-fusion.com/atlantis/episodes/293/319_l-equilibre-parfait.html',
    'https://www.stargate-fusion.com/atlantis/episodes/294/320_nom-de-code-horizon.html']
data_S03_SGA = []
for page_episode_S03_SGA in pages_episodes_S03_SGA :
    ep_S03_SGA = []
    response_S03_SGA = requests.get(page_episode_S03_SGA)
    soup_S03_SGA = bs4.BeautifulSoup(response_S03_SGA.text, 'html.parser')
    info_epi_S03_SGA = soup_S03_SGA.find_all("font")
    for epi_S03_SGA in info_epi_S03_SGA :
        ep_S03_SGA.append(epi_S03_SGA.next_sibling)
    data_S03_SGA.append(ep_S03_SGA)
#print(data_S03_SGA)

episodes_S03_SGA = []
for d_S03_SGA in data_S03_SGA :
    episode_S03_SGA = {
        'title': d_S03_SGA[0],
        'epi_num': d_S03_SGA[1],
        'diffusion_date': d_S03_SGA[2],
        'audience_us' : d_S03_SGA[3],
        'audience_fr' : d_S03_SGA[4],
        'scenarist' : d_S03_SGA[5],
        'director': d_S03_SGA[6]
        }
    episodes_S03_SGA.append(episode_S03_SGA)
print(episodes_S03_SGA)
