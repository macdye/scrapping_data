import requests
import bs4
import re

pages_episodes_S08_SG1 = [
    'https://www.stargate-fusion.com/sg1/episodes/154/801_mesalliance-1-2.html',
    'https://www.stargate-fusion.com/sg1/episodes/155/802_mesalliance-2-2.html',
    'https://www.stargate-fusion.com/sg1/episodes/156/803_quarantaine.html',
    'https://www.stargate-fusion.com/sg1/episodes/157/804_heure-h.html',
    'https://www.stargate-fusion.com/sg1/episodes/158/805_le-feu-aux-poudres.html',
    'https://www.stargate-fusion.com/sg1/episodes/159/806_avatar.html',
    'https://www.stargate-fusion.com/sg1/episodes/161/807_monde-cruel.html',
    'https://www.stargate-fusion.com/sg1/episodes/160/808_aux-yeux-du-monde.html',
    'https://www.stargate-fusion.com/sg1/episodes/162/809_discordes.html',
    'https://www.stargate-fusion.com/sg1/episodes/163/810_sans-pitie.html',
    'https://www.stargate-fusion.com/sg1/episodes/219/811_vulnerable.html',
    'https://www.stargate-fusion.com/sg1/episodes/164/812_en-detresse.html',
    'https://www.stargate-fusion.com/sg1/episodes/165/813_une-vieille-connaissance.html',
    'https://www.stargate-fusion.com/sg1/episodes/202/814_alerte-maximum.html',
    'https://www.stargate-fusion.com/sg1/episodes/206/815_rien-a-perdre.html',
    'https://www.stargate-fusion.com/sg1/episodes/203/816_la-derniere-chance-1-2.html',
    'https://www.stargate-fusion.com/sg1/episodes/204/817_la-derniere-chance-2-2.html',
    'https://www.stargate-fusion.com/sg1/episodes/205/818_pour-la-vie.html',
    'https://www.stargate-fusion.com/sg1/episodes/207/819_retour-vers-le-futur-1-2.html',
    'https://www.stargate-fusion.com/sg1/episodes/208/820_retour-vers-le-futur-2-2.html']
data_S08_SG1 = []
for page_episode_S08_SG1 in pages_episodes_S08_SG1 :
    ep_S08_SG1 = []
    response_S08_SG1 = requests.get(page_episode_S08_SG1)
    soup_S08_SG1 = bs4.BeautifulSoup(response_S08_SG1.text, 'html.parser')
    info_epi_S08_SG1 = soup_S08_SG1.find_all("font")
    for epi_S08_SG1 in info_epi_S08_SG1 :
        ep_S08_SG1.append(epi_S08_SG1.next_sibling)
    data_S08_SG1.append(ep_S08_SG1)
#print(data_S08_SG1)

episodes_S08_SG1 = []
for d_S08_SG1 in data_S08_SG1 :
    episode_S08_SG1 = {
        'title': d_S08_SG1[0],
        'epi_num': d_S08_SG1[1],
        'diffusion_date': d_S08_SG1[2],
        'audience_us' : d_S08_SG1[3],
        'audience_fr' : d_S08_SG1[4],
        'scenarist' : d_S08_SG1[5],
        'director' : d_S08_SG1[6]
        }
    episodes_S08_SG1.append(episode_S08_SG1)
print(episodes_S08_SG1)
