import requests
import bs4
import re

"""pages_epi_spe = ['https://www.stargate-fusion.com/sg1/personnages/81/ba-al.html','https://www.stargate-fusion.com/sg1/cultures/4/asgards.html','https://www.stargate-fusion.com/sg1/cultures/64/tok-ras.html','https://www.stargate-fusion.com/atlantis/personnages/738/todd.html']
for i in pages_epi_spe:
    response2 = requests.get(i)
    soup2 = bs4.BeautifulSoup(response2.text, 'html.parser')
    epi_spe = soup2.find_all("span", {"class":"liste_epi"})
    print(epi_spe) """

pages_episodes = ['https://www.stargate-fusion.com/atlantis/episodes/222/201_sous-le-feu-de-l-ennemi.html',
'https://www.stargate-fusion.com/atlantis/episodes/231/202_i-a.html',
'https://www.stargate-fusion.com/atlantis/episodes/220/203_chasse-a-l-homme.html',
'https://www.stargate-fusion.com/atlantis/episodes/227/204_a-corps-perdu.html',
'https://www.stargate-fusion.com/atlantis/episodes/237/205_les-condamnes.html',
'https://www.stargate-fusion.com/atlantis/episodes/221/206_l-experience-interdite.html',
'https://www.stargate-fusion.com/atlantis/episodes/239/207_instinct.html',
'https://www.stargate-fusion.com/atlantis/episodes/238/208_mutation.html',
'https://www.stargate-fusion.com/atlantis/episodes/230/209_l-aurore.html',
'https://www.stargate-fusion.com/atlantis/episodes/251/210_l-union-fait-la-force-1-2.html',
'https://www.stargate-fusion.com/atlantis/episodes/252/211_l-union-fait-la-force-2-2.html',
'https://www.stargate-fusion.com/atlantis/episodes/232/212_tempus-fugit.html',
'https://www.stargate-fusion.com/atlantis/episodes/242/213_masse-critique.html',
'https://www.stargate-fusion.com/atlantis/episodes/253/214_l-ivresse-des-profondeurs.html',
'https://www.stargate-fusion.com/atlantis/episodes/254/215_la-tour.html',
'https://www.stargate-fusion.com/atlantis/episodes/256/216_possedes.html',
'https://www.stargate-fusion.com/atlantis/episodes/257/217_coup-d-etat.html',
'https://www.stargate-fusion.com/atlantis/episodes/255/218_traitement-de-choc.html',
'https://www.stargate-fusion.com/atlantis/episodes/259/219_inferno.html',
'https://www.stargate-fusion.com/atlantis/episodes/260/220_les-allies.html']
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

