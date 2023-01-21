from bs4 import BeautifulSoup
import requests
from csv import writer

with open('monsters.csv', 'w', newline='') as f_object:
	for i in range(1, 15):	
		pagenum = str(i)
		URL = "https://2e.aonprd.com/Monsters.aspx?ID=" + pagenum

		r = requests.get(URL)

		if(r.status_code == 200):
			soup = BeautifulSoup(r.content, 'html.parser')
			div_contain = soup.find("div", {"class":"main"})
			name = div_contain.find("h1", {"class":"title"}).get_text(strip=True)
			cr = name.find("span")

			monsters=[cr, name, URL]

			wobj = writer(f_object)
			wobj.writerow(monsters)
			#print(name)
			#print(cr)
			#print(URL)
			#print("------------------")

		else:
			continue
	
		