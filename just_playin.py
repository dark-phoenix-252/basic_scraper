import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs


def retrieve_links(url):

	# HTML --> BS Object
	html = urlopen(url)
	bsObj = bs(html.read(), 'lxml')

	# Menu_List_CSV
	fields = ['Topic', 'URL']
	menu_List = bsObj.find_all('a', href=True)
	with open('gfk_lists.csv', 'w', encoding='utf-8') as filename:
	    csvwritter = csv.writer(filename, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
	    csvwritter.writerow(fields)
	    for lists in menu_List:
	        csvwritter.writerow(lists.text)
	        csvwritter.writerow(lists.get('href')) 


retrieve_links("https://geeksforgeeks.org")






        

        













