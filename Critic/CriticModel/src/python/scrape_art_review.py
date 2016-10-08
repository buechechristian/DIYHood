from lxml import html
import requests, sys, re, string

def write_review_to_file(url):
	filename = url.replace('http://artandcritique.com/', '../../data/review')[:-1] + '.txt'
	try:
		page = requests.get(url)
	except Exception as err:
		print('Error: ' + str(err))
		quit()
	tree = html.fromstring(page.text)
	p_elems = tree.xpath('//*/div/div/p')
	paragraphs = [];
	for p in p_elems:
		if p.text != None:
			paragraphs.append(p.text)
	output_text = string.join((paragraphs[1:])[:-1], '\n').encode('utf-8')
	print 'Writing ' + filename;
	file = open(filename, 'w')
	file.write(output_text)
	file.close()

for url in sys.argv[1:]:
	write_review_to_file(url)


