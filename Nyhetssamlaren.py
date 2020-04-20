#! python3


import requests
from bs4 import BeautifulSoup
from gensim.summarization import summarize

url = 'https://www.gp.se/nyheter/sverige/sverige-%C3%A4ndrar-inte-strategi-trots-who-besked-1.26396387'
page = requests.get(url).text

soup = BeautifulSoup(page)

headline = soup.find('h1').get_text()
print(headline)

p_tags = soup.find_all('p')

p_tags_text = [tag.get_text().strip() for tag in p_tags]
p_tags_text

sentence_list = [sentence for sentence in p_tags_text if not '\n' in sentence]
sentence_list = [sentence for sentence in sentence_list if '.' in sentence]
sentence_list

article = ' '.join(sentence_list)

summary = summarize(article, ratio=0.3)


print(f'Length of original article: {len(article)}')
print(f'Length of summary: {len(summary)} \n')
print(f'Headline: {headline} \n')
print(f'Article Summary:\n{summary}')
print("Press enter to exit")
input()
