import requests
import bs4
import re

pages_episodes_S09_SG1 = [
    'https://www.stargate-fusion.com/sg1/episodes/224/901_le-tresor-d-avalon-1-2.html',
    'https://www.stargate-fusion.com/sg1/episodes/225/902_le-tresor-d-avalon-2-2.html',
    'https://www.stargate-fusion.com/sg1/episodes/226/903_le-livre-des-origines.html',
    'https://www.stargate-fusion.com/sg1/episodes/223/904_ce-lien-qui-nous-unit.html',
    'https://www.stargate-fusion.com/sg1/episodes/228/905_proselytisme.html',
    'https://www.stargate-fusion.com/sg1/episodes/240/906_le-piege.html',
    'https://www.stargate-fusion.com/sg1/episodes/233/907_terre-d-asile.html',
    'https://www.stargate-fusion.com/sg1/episodes/236/908_pour-l-honneur.html',
    'https://www.stargate-fusion.com/sg1/episodes/243/909_prototype.html',
    'https://www.stargate-fusion.com/sg1/episodes/234/910_le-4eme-cavalier-de-l-apocalypse-1-2.html',
    'https://www.stargate-fusion.com/sg1/episodes/235/911_le-4eme-cavalier-de-l-apocalypse-2-2.html',
    'https://www.stargate-fusion.com/sg1/episodes/241/912_dommage-collateral.html',
    'https://www.stargate-fusion.com/sg1/episodes/245/913_effet-domino.html',
    'https://www.stargate-fusion.com/sg1/episodes/246/914_prise-de-controle.html',
    'https://www.stargate-fusion.com/sg1/episodes/247/915_ingerence.html',
    'https://www.stargate-fusion.com/sg1/episodes/248/916_hors-limite.html',
    'https://www.stargate-fusion.com/sg1/episodes/249/917_le-chatiment.html',
    'https://www.stargate-fusion.com/sg1/episodes/250/918_le-manteau-d-arthur.html',
    'https://www.stargate-fusion.com/sg1/episodes/229/919_la-grande-croisade.html',
    'https://www.stargate-fusion.com/sg1/episodes/258/920_la-premiere-vague.html']
data_S09_SG1 = []
for page_episode_S09_SG1 in pages_episodes_S09_SG1 :
    ep_S09_SG1 = []
    response_S09_SG1 = requests.get(page_episode_S09_SG1)
    soup_S09_SG1 = bs4.BeautifulSoup(response_S09_SG1.text, 'html.parser')
    info_epi_S09_SG1 = soup_S09_SG1.find_all("font")
    for epi_S09_SG1 in info_epi_S09_SG1 :
        ep_S09_SG1.append(epi_S09_SG1.next_sibling)
    data_S09_SG1.append(ep_S09_SG1)
#print(data_S09_SG1)

episodes_S09_SG1 = []
for d_S09_SG1 in data_S09_SG1 :    
    episode_S09_SG1 = {
        'titre' : d_S09_SG1[0],
        'numero' : d_S09_SG1[1],
        'date de diffusion' : d_S09_SG1[2],
        'audience_us' : d_S09_SG1[3],
        'audience_fr' : d_S09_SG1[4],
        'scenariste' : d_S09_SG1[5],
        'realisateur' : d_S09_SG1[6]
        }
    episodes_S09_SG1.append(episode_S09_SG1)
print(episodes_S09_SG1)

