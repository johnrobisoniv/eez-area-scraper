# A script to generate a csv of EEZs from a table on wikipedia
from bs4 import BeautifulSoup
import urllib2


def get_eez_areas (output_filename):
    response = urllib2.urlopen('https://en.wikipedia.org/wiki/Exclusive_economic_zone')
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')

    table = soup.find(id='Rankings_by_area').find_parent().next_sibling.next_sibling.next_sibling.next_sibling
    rows = table.find_all('tr')


    outfile = open(output_filename, 'w')

    #print rows[2]
    count = 0
    for row in rows:
        if count != 0:
            cells = row.find_all('td')
            country = cells[1].a.string
            eez_area = cells[2].string
            try:
                outfile.write(country + ',' + str(int(eez_area.replace(',',''))) + '\n')
            except:
                pass
            #print cells
        count += 1
    outfile.close()


def main():
    get_eez_areas('out.csv')

if __name__ == '__main__':
    main()
