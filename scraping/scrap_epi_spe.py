import requests
import bs4
import re

# pages_epi_spe = ['https://www.stargate-fusion.com/sg1/personnages/81/ba-al.html','https://www.stargate-fusion.com/sg1/cultures/4/asgards.html','https://www.stargate-fusion.com/sg1/cultures/64/tok-ras.html','https://www.stargate-fusion.com/atlantis/personnages/738/todd.html']
# for i in pages_epi_spe:
#     response = requests.get(i)
#     soup = bs4.BeautifulSoup(response.text, 'html.parser')
#     epi_spe = soup.find_all("span", {"class":"liste_epi"})
#     print(epi_spe)