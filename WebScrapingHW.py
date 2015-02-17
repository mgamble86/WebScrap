curl 'https://www.eeb.ucla.edu/seminars.php?id=[1-800]' > [1-800].html

!# usr/bin/python

from bs4 import BeautifulSoup

soup = BeautifulSoup(open('1.html'))

main_pane = soup.find_all(id='main-content')


#Below DOES NOT WORK - tried to isolate EcoEvoPub
#There are too many texts items all called <p>, with no other identifier to specify which one I want for names.
#I don't think this is possible based on how the webpage is coded.

my_file = open('ecoevo.txt', 'a')

for div in main_pane:
	section_class = div.find('div', class_='section')
	ecoevo = section_class.strong
	if ecoevo == 'EcoEvoPub Series':
	    for div in main_pane:
		    section_class = div.find('div', class_='section')
			date = section_class.h4
			name = section_class.p
        my_file.write(str(date + " " + name)
    elif ecoevo != 'EcoEvoPub.Series':
	    continue
		
		
# This only prints all the seminar dates, but worked

my_file = open('ecoevo.txt', 'a')

for div in main_pane:
    section_class = div.find('div', class_='section')
    date = section_class.h4
    my_file.write(str(date))