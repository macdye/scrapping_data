import requests
import bs4
import re

pages_episodes_S01_SGA = [
    'https://www.stargate-fusion.com/atlantis/episodes/166/101_une-nouvelle-ere-1-2.html',
    'https://www.stargate-fusion.com/atlantis/episodes/167/102_une-nouvelle-ere-2-2.html',
    'https://www.stargate-fusion.com/atlantis/episodes/168/103_invulnerable.html',
    'https://www.stargate-fusion.com/atlantis/episodes/169/104_38-minutes.html',
    'https://www.stargate-fusion.com/atlantis/episodes/170/105_soupcons.html',
    'https://www.stargate-fusion.com/atlantis/episodes/171/106_la-fin-de-l-innocence.html',
    'https://www.stargate-fusion.com/atlantis/episodes/172/107_serum.html',
    'https://www.stargate-fusion.com/atlantis/episodes/174/108_apparences.html',
    'https://www.stargate-fusion.com/atlantis/episodes/173/109_retour-sur-terre.html',
    'https://www.stargate-fusion.com/atlantis/episodes/175/110_en-pleine-tempete-1-2.html',
    'https://www.stargate-fusion.com/atlantis/episodes/176/111_en-pleine-tempete-2-2.html',
    'https://www.stargate-fusion.com/atlantis/episodes/209/112_duel.html',
    'https://www.stargate-fusion.com/atlantis/episodes/212/113_virus.html',
    'https://www.stargate-fusion.com/atlantis/episodes/211/114_hors-d-atteinte.html',
    'https://www.stargate-fusion.com/atlantis/episodes/213/115_le-grand-sommeil.html',
    'https://www.stargate-fusion.com/atlantis/episodes/214/116_la-communaute-des-quinze.html',
    'https://www.stargate-fusion.com/atlantis/episodes/215/117_derniers-messages.html',
    'https://www.stargate-fusion.com/atlantis/episodes/218/118_sous-hypnose.html',
    'https://www.stargate-fusion.com/atlantis/episodes/216/119_assieges-1-2.html',
    'https://www.stargate-fusion.com/atlantis/episodes/217/120_assieges-2-2.html']
data_S01_SGA = []
for page_episode_S01_SGA in pages_episodes_S01_SGA :
    ep_S01_SGA = []
    response_S01_SGA = requests.get(page_episode_S01_SGA)
    soup_S01_SGA = bs4.BeautifulSoup(response_S01_SGA.text, 'html.parser')
    info_epi_S01_SGA = soup_S01_SGA.find_all("font")
    for epi_S01_SGA in info_epi_S01_SGA :
        ep_S01_SGA.append(epi_S01_SGA.next_sibling)
    data_S01_SGA.append(ep_S01_SGA)
#print(data_S01_SGA)

episodes_S01_SGA = []
for d_S01_SGA in data_S01_SGA :    
    episode_S01_SGA = {
        'titre' : d_S01_SGA[0],
        'numero' : d_S01_SGA[1],
        'date de diffusion' : d_S01_SGA[2],
        'audience_us' : d_S01_SGA[3],
        'audience_fr' : d_S01_SGA[4],
        'scenariste' : d_S01_SGA[5],
        'realisateur' : d_S01_SGA[6]
        }
    episodes_S01_SGA.append(episode_S01_SGA)
print(episodes_S01_SGA)
