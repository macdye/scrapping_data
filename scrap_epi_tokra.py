import requests
import bs4
import re

pages_episodes_S10_SG1 = [
    'https://www.stargate-fusion.com/sg1/episodes/23/202_la-tete-a-l-envers.html',
    'https://www.stargate-fusion.com/sg1/episodes/32/211_la-tok-ra-1-2.html',
    'https://www.stargate-fusion.com/sg1/episodes/33/212_la-tok-ra-2-2.html',
    'https://www.stargate-fusion.com/sg1/episodes/39/218_la-colere-des-dieux.html',
    'https://www.stargate-fusion.com/sg1/episodes/41/220_l-ennemi-invisible.html',
    'https://www.stargate-fusion.com/sg1/episodes/44/301_dans-l-antre-des-goa-ulds.html',
    'https://www.stargate-fusion.com/sg1/episodes/45/302_seth.html',
    'https://www.stargate-fusion.com/sg1/episodes/55/312_les-flammes-de-l-enfer-1-2.html',
    'https://www.stargate-fusion.com/sg1/episodes/56/313_les-flammes-de-l-enfer-2-2.html',
    'https://www.stargate-fusion.com/sg1/episodes/58/315_simulation.html',
    'https://www.stargate-fusion.com/sg1/episodes/68/403_experimentation-hasardeuse.html',
    'https://www.stargate-fusion.com/sg1/episodes/69/404_destins-croises.html',
    'https://www.stargate-fusion.com/sg1/episodes/70/405_divisez-pour-conquerir.html'
    'https://www.stargate-fusion.com/sg1/episodes/77/412_perdus-dans-l-espace.html',
    'https://www.stargate-fusion.com/sg1/episodes/79/414_le-venin-du-serpent.html',
    'https://www.stargate-fusion.com/sg1/episodes/82/417_pouvoir-absolu.html',
    'https://www.stargate-fusion.com/sg1/episodes/87/422_exode.html',
    'https://www.stargate-fusion.com/sg1/episodes/88/501_ennemis-jures.html',
    'https://www.stargate-fusion.com/sg1/episodes/102/515_sans-issue-1-2.html',
    'https://www.stargate-fusion.com/sg1/episodes/103/516_sans-issue-2-2.html',
    'https://www.stargate-fusion.com/sg1/episodes/112/603_reunion.html',
    'https://www.stargate-fusion.com/sg1/episodes/113/604_prisonniere-des-glaces.html',
    'https://www.stargate-fusion.com/sg1/episodes/115/606_abysse.html',
    'https://www.stargate-fusion.com/sg1/episodes/118/609_l-union-fait-la-force.html',
    'https://www.stargate-fusion.com/sg1/episodes/119/610_la-reine.html',
    'https://www.stargate-fusion.com/sg1/episodes/124/615_paradis-perdu.html',
    'https://www.stargate-fusion.com/sg1/episodes/142/711_la-fontaine-de-jouvence-1-2.html',
    'https://www.stargate-fusion.com/sg1/episodes/143/712_la-fontaine-de-jouvence-2-2.html',
    'https://www.stargate-fusion.com/sg1/episodes/144/713_le-voyage-interieur.html',
    'https://www.stargate-fusion.com/sg1/episodes/147/716_la-fin-de-l-union.html',
    'https://www.stargate-fusion.com/sg1/episodes/203/816_la-derniere-chance-1-2.html',
    'https://www.stargate-fusion.com/sg1/episodes/204/817_la-derniere-chance-2-2.html',
    'https://www.stargate-fusion.com/sg1/episodes/205/818_pour-la-vie.html']
data_S10_SG1 = []
for page_episode_S10_SG1 in pages_episodes_S10_SG1 :
    ep_S10_SG1 = []
    response_S10_SG1 = requests.get(page_episode_S10_SG1)
    soup_S10_SG1 = bs4.BeautifulSoup(response_S10_SG1.text, 'html.parser')
    info_epi_S10_SG1 = soup_S10_SG1.find_all("font")
    for epi_S10_SG1 in info_epi_S10_SG1 :
        ep_S10_SG1.append(epi_S10_SG1.next_sibling)
    data_S10_SG1.append(ep_S10_SG1)
#print(data_S10_SG1)

episodes_S10_SG1 = []
for d_S10_SG1 in data_S10_SG1 :    
    episode_S10_SG1 = {
        'titre' : d_S10_SG1[0],
        'numero' : d_S10_SG1[1],
        'date de diffusion' : d_S10_SG1[2],
        'audience_us' : d_S10_SG1[3],
        'audience_fr' : d_S10_SG1[4],
        'scenariste' : d_S10_SG1[5],
        'realisateur' : d_S10_SG1[6]
        }
    episodes_S10_SG1.append(episode_S10_SG1)
print(episodes_S10_SG1)

