from bs4 import BeautifulSoup
from query import simple_get
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords # Filter out stopwords, such as 'the', 'or', 'and'
import re

def get_job_postings(soup, job_urls):
  job_headings = soup.find_all('div', {'class': 'title'})
  for heading in job_headings:
    url = heading.find('a' , recursive=False).get('href')
    job_urls.append(f'https://www.indeed.ca{url}')

def scrape_indeed_feed(url, page, job_urls):
  raw_html = simple_get(f"{url}&start={page * 15}")
  soup = BeautifulSoup(raw_html, 'html.parser')
  get_job_postings(soup, job_urls)

def create_list_of_words(bullets, bullet_words):
  for bullet in bullets:
    text = bullet.get_text()

    # clean up text, from https://jessesw.com/Data-Science-Skills/    
    text = re.sub("[^a-zA-Z.+3]"," ", text) # Now get rid of any terms that aren't words (include 3 for d3.js)
                                            # Also include + for C++
        
    text = text.lower().split()  # Go to lower case and split apart
        
    stop_words = set(stopwords.words("english")) # Filter out any stop words
    text = [w for w in text if not w in stop_words]

    text = list(set(text)) # Last, just get the set of these. Ignore counts (we are just looking at whether a term existed
                            # or not on the website)
    bullet_words.extend(text)

def scrape_indeed_job_page(url, job_words):  
  raw_html = simple_get(url)
  soup = BeautifulSoup(raw_html, 'html.parser')
  bullets = soup.find_all('li')
  bullet_words = []
  create_list_of_words(bullets, bullet_words)
  job_words.extend(bullet_words)