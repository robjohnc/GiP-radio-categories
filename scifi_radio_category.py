#!/usr/bin/python
import requests
import bs4
import subprocess

def get_programme_links(page_url):
	data = {}
	response = requests.get(page_url)
	soup = bs4.BeautifulSoup(response.text)
	#get URLs from page
	data['links'] = [a.attrs.get('resource') for a in soup.select('h4.programme__titles a[href^=/programmes]')]
	#get URL to "Next" page link
	data['pages'] = [a.attrs.get('href') for a in soup.select('li.pagination__next a[href^=/radio]')]
	return data


compiled_data = {}
compiled_data['links']=[]
data = get_programme_links('http://www.bbc.co.uk/radio/programmes/genres/drama/scifiandfantasy/player/episodes')
#data = get_programme_links('http://www.bbc.co.uk/radio/programmes/genres/drama/horrorandsupernatural/player/episodes')
compiled_data['links'] += data['links']


#iterate through following pages, if any
while data['pages']:
	data = get_programme_links('http://www.bbc.co.uk'+ data['pages'][0])
	compiled_data['links'] += data['links']

#pull PIDs from gathered URLs and push them through to get_iplayer 
for link in compiled_data['links']:
	pid = link.split("/")[4]
	#print pid
	execstring="get_iplayer --type=radio --pid="+ pid
	process = subprocess.Popen(execstring.split(), stdout=subprocess.PIPE)
	output = process.communicate()[0]
