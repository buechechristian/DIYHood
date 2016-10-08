from lxml import html
import requests, os, sys, argparse, string

# Get argument values
parser = argparse.ArgumentParser(description='Scrape all articles from an archive page')
parser.add_argument('arg_url', metavar='A', type=str, nargs=1,  help='The letter index')

args = vars(parser.parse_args())

url = args['arg_url'][0]

# Get page
page = requests.get(url)
tree = html.fromstring(page.text)

# Get links
links = tree.xpath('//*[@id="post-4"]/div[2]/div/p/a/@href')

review_links = [k for k in links if 'http' in k]

print string.join(review_links, '\n')