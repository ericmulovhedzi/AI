# hello.py

import re
import requests
from bs4 import BeautifulSoup

sentence = 'The man who passes \
the sentence should swing the sword.'

url = 'https://www.gutenberg.org/files/766/766-0.txt'
#url = 'https://www.gutenberg.org/files/{}/{}.txt'
#url = 'https://imbobo.org.za'
#url = 'https://www.farosian.com'
#url = 'https://dartcom.co.za'
#url = 'https://www.gutenberg.org/files/{}/{}-0.txt'

tokens = re.sub(r'([^\s\w]|_)+', ' ',sentence).split()

#print(tokens)

# Extracting n-grams using customed defined function
def n_gram_extractor(sentence, n):
	tokens = re.sub(r'([^\s\w]|_)+', ' ',sentence).split()
	for i in range(len(tokens)-n+1):
		print(tokens[i:i+n])
		

def http_request(url):
	r = requests.post(url)
	print('')
	print('------ ELT Processing ------')
	print('')
	print('Lod from URL: ',url)
	#print(r.text[:0])
	print('HTTP response status code: ',r.status_code)
	#print(r.text[:0])
	
	file_name = url[len(url) -10:]
	with open ("data/html/"+file_name, "w", encoding="utf-8") as f:
		f.write(r.text)
		
	soup = BeautifulSoup(open("data/html/"+file_name), 'html.parser')
	
	#print('No of Links: ')
	#print(len(soup.find_all('a')))
	#print('No of Images: ')
	#print(len(soup.find_all('img')))
	#print('No of Headers(h1): ')
	#print(len(soup.find_all('h1')))
	
	#print("No of Images: "+len(soup.find_all('img')))
	#print("No of Headers(1): "+len(soup.find_all('h1')))
	
	#print(soup.find("h2").string)
	
	print('')
	
#n_gram_extractor(sentence,2)

http_request(url)

print('Lod from FILE: "data/csv/pg_catalog.csv":')
	
with open('data/csv/pg_catalog.csv') as file:
	content = file.readlines()
header = content[:1]
rows = content[1:]
print(header)
#print(rows)
print('')
print('------ ------ ------')
print('')