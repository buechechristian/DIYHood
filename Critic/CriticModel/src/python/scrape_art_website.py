
from lxml import html
import requests, sys, re, string

def find_archive_urls():
	urls = []
	for yyyy in ['2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']:
		for mm in ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']:
			url = 'http://artandcritique.com/' + yyyy + '/' + mm
			if requests.get(url).status_code == 200:
				print 'Found url ' + url
				urls.append(url)
	return urls

def find_page_urls(archive_url):
	try:
		page = requests.get(archive_url)
	except Exception as err:
		print('Error: ' + str(err))
		quit()
	tree = html.fromstring(page.text)
	links = tree.xpath('//*/header/div/h2/a/@href')
	return links

archive_urls = find_archive_urls()
# archive_urls = ['http://artandcritique.com/2009/09', 'http://artandcritique.com/2009/11', 'http://artandcritique.com/2011/06']
page_urls = []
for url in archive_urls:
	page_urls = page_urls + find_page_urls(url)

for url in page_urls:
	print url
