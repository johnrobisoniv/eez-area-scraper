# A script to generate a csv of EEZs from a table on wikipedia
from bs4 import BeautifulSoup
import urllib2


def get_eez_areas (output_filename):

    # First, use urllib2 to read the html into a BeautifulSoup object
    response = urllib2.urlopen('https://en.wikipedia.org/wiki/Exclusive_economic_zone')
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')

    # Then, traverse the DOM to find the appropriate table, and read the rows into an array
    table = soup.find(id='Rankings_by_area').find_parent().next_sibling.next_sibling.next_sibling.next_sibling
    rows = table.find_all('tr')


    # Set up our outfile to accept data as we iterate through the rows array
    outfile = open(output_filename, 'w')

    # Iterate through the rows, writing each country, value pair to a new line
    # in our outfile - csv format
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

    # Close the outfile
    outfile.close()


def main():
    get_eez_areas('out.csv')

if __name__ == '__main__':
    main()
