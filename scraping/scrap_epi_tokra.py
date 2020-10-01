import requests
import bs4
import re

pages_episodes_tokra = [
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
data_tokra = []
for page_episode_tokra in pages_episodes_tokra :
    ep_tokra = []
    response_tokra = requests.get(page_episode_tokra)
    soup_tokra = bs4.BeautifulSoup(response_tokra.text, 'html.parser')
    info_epi_tokra = soup_tokra.find_all("font")
    for epi_tokra in info_epi_tokra :
        ep_tokra.append(epi_tokra.next_sibling)
    data_tokra.append(ep_tokra)
#print(data_tokra)

episodes_tokra = []
for d_tokra in data_tokra :
    episode_tokra = {
        'title': d_tokra[0],
        'epi_num': d_tokra[1],
        'diffusion_date': d_tokra[2],
        'audience_us' : d_tokra[3],
        'audience_fr' : d_tokra[4],
        'scenarist' : d_tokra[5],
        'director': d_tokra[6]
        }
    episodes_tokra.append(episode_tokra)
print(episodes_tokra)

