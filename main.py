import requests
import csv
from bs4 import BeautifulSoup

def main():
    dials = []
    for i in range(0,1000,10):
        r = requests.get("http://localhost:31337/WebPro.htm%3FsessionId%3D9561%26SDKEY(0%2C"+str(i)+")")
        soup = BeautifulSoup(r.text, "html.parser")
        table = soup.find("form", attrs={'name':'theDataForm'}).find("table", attrs={'class': 'standard'}).find("td", attrs={'class': 't'}).find("table")
        rows = table.find_all('tr')
        for row in rows[3:]:
            cols = row.find_all('td')
            speeddial = cols[0].text
            number = cols[1].find("input").attrs['value']
            name = cols[2].find("input").attrs['value']

            if number != '' or name != '':
                dials.append((speeddial,number,name,))
                print(speeddial,number,name,)

    with open('output.csv', 'w') as f:
        writer = csv.writer(f)
        for dial in dials:
            writer.writerow(dial)
        

if __name__ == "__main__":
    main()
