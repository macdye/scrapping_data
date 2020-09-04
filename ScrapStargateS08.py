import requests
import bs4
import re

"""pages_epi_spe = ['https://www.stargate-fusion.com/sg1/personnages/81/ba-al.html','https://www.stargate-fusion.com/sg1/cultures/4/asgards.html','https://www.stargate-fusion.com/sg1/cultures/64/tok-ras.html','https://www.stargate-fusion.com/atlantis/personnages/738/todd.html']
for i in pages_epi_spe:
    response2 = requests.get(i)
    soup2 = bs4.BeautifulSoup(response2.text, 'html.parser')
    epi_spe = soup2.find_all("span", {"class":"liste_epi"})
    print(epi_spe) """

pages_episodes = ['https://www.stargate-fusion.com/sg1/episodes/154/801_mesalliance-1-2.html',
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

