import requests
import bs4
import re

"""pages_epi_spe = ['https://www.stargate-fusion.com/sg1/personnages/81/ba-al.html','https://www.stargate-fusion.com/sg1/cultures/4/asgards.html','https://www.stargate-fusion.com/sg1/cultures/64/tok-ras.html','https://www.stargate-fusion.com/atlantis/personnages/738/todd.html']
for i in pages_epi_spe:
    response2 = requests.get(i)
    soup2 = bs4.BeautifulSoup(response2.text, 'html.parser')
    epi_spe = soup2.find_all("span", {"class":"liste_epi"})
    print(epi_spe) """

pages_episodes = ['https://www.stargate-fusion.com/sg1/episodes/224/901_le-tresor-d-avalon-1-2.html',
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

