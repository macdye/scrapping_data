import requests
import bs4
import re

"""pages_epi_spe = ['https://www.stargate-fusion.com/sg1/personnages/81/ba-al.html','https://www.stargate-fusion.com/sg1/cultures/4/asgards.html','https://www.stargate-fusion.com/sg1/cultures/64/tok-ras.html','https://www.stargate-fusion.com/atlantis/personnages/738/todd.html']
for i in pages_epi_spe:
    response2 = requests.get(i)
    soup2 = bs4.BeautifulSoup(response2.text, 'html.parser')
    epi_spe = soup2.find_all("span", {"class":"liste_epi"})
    print(epi_spe) """

pages_episodes = ['https://www.stargate-fusion.com/sg1/episodes/261/1001_l-oricy.html','https://www.stargate-fusion.com/sg1/episodes/267/1002_dans-les-bras-de-morphee.html','https://www.stargate-fusion.com/sg1/episodes/268/1003_chasse-croise.html','https://www.stargate-fusion.com/sg1/episodes/269/1004_la-guerre-des-clones.html','https://www.stargate-fusion.com/sg1/episodes/270/1005_la-creature.html','https://www.stargate-fusion.com/sg1/episodes/271/1006_wormhole-x-treme-le-film.html','https://www.stargate-fusion.com/sg1/episodes/272/1007_la-riposte.html','https://www.stargate-fusion.com/sg1/episodes/273/1008_amnesie.html','https://www.stargate-fusion.com/sg1/episodes/274/1009_aux-mains-des-rebelles.html','https://www.stargate-fusion.com/sg1/episodes/275/1010_la-quete-du-graal-1-2.html']
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

