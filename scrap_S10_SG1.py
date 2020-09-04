import requests
import bs4
import re

# pages_epi_spe = ['https://www.stargate-fusion.com/sg1/personnages/81/ba-al.html','https://www.stargate-fusion.com/sg1/cultures/4/asgards.html','https://www.stargate-fusion.com/sg1/cultures/64/tok-ras.html','https://www.stargate-fusion.com/atlantis/personnages/738/todd.html']
# for i in pages_epi_spe:
#     response = requests.get(i)
#     soup = bs4.BeautifulSoup(response.text, 'html.parser')
#     epi_spe = soup.find_all("span", {"class":"liste_epi"})
#     print(epi_spe)

pages_episodes_S10_SG1 = [
    'https://www.stargate-fusion.com/sg1/episodes/261/1001_l-oricy.html',
    'https://www.stargate-fusion.com/sg1/episodes/267/1002_dans-les-bras-de-morphee.html',
    'https://www.stargate-fusion.com/sg1/episodes/268/1003_chasse-croise.html',
    'https://www.stargate-fusion.com/sg1/episodes/269/1004_la-guerre-des-clones.html',
    'https://www.stargate-fusion.com/sg1/episodes/270/1005_la-creature.html',
    'https://www.stargate-fusion.com/sg1/episodes/271/1006_wormhole-x-treme-le-film.html',
    'https://www.stargate-fusion.com/sg1/episodes/272/1007_la-riposte.html',
    'https://www.stargate-fusion.com/sg1/episodes/273/1008_amnesie.html',
    'https://www.stargate-fusion.com/sg1/episodes/274/1009_aux-mains-des-rebelles.html',
    'https://www.stargate-fusion.com/sg1/episodes/275/1010_la-quete-du-graal-1-2.html',
    'https://www.stargate-fusion.com/sg1/episodes/276/1011_la-quete-du-graal-2-2.html',
    'https://www.stargate-fusion.com/sg1/episodes/279/1012_la-grande-illusion.html',
    'https://www.stargate-fusion.com/sg1/episodes/295/1013_dimension-parallele.html',
    'https://www.stargate-fusion.com/sg1/episodes/278/1014_question-de-confiance.html',
    'https://www.stargate-fusion.com/sg1/episodes/277/1015_morts-ou-vifs.html',
    'https://www.stargate-fusion.com/sg1/episodes/296/1016_prise-d-otages.html',
    'https://www.stargate-fusion.com/sg1/episodes/297/1017_la-loi-du-talion.html',
    'https://www.stargate-fusion.com/sg1/episodes/298/1018_un-air-de-famille.html',
    'https://www.stargate-fusion.com/sg1/episodes/299/1019_la-symbiose-du-mal.html',
    'https://www.stargate-fusion.com/sg1/episodes/300/1020_le-temps-d-une-vie.html']
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

