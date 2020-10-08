import requests
import bs4
import re

pages_episodes_S02_SGA = [
    'https://www.stargate-fusion.com/atlantis/episodes/222/201_sous-le-feu-de-l-ennemi.html',
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
        'title': d_S02_SGA[0],
        'epi_num': d_S02_SGA[1],
        'diffusion_date': d_S02_SGA[2],
        'audience_us' : d_S02_SGA[3],
        'audience_fr' : d_S02_SGA[4],
        'scenarist' : d_S02_SGA[5],
        'director': d_S02_SGA[6]
        }
    episodes_S02_SGA.append(episode_S02_SGA)
#print(episodes_S02_SGA)

