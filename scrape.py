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
  raw_html = simple_get(f"{url}&start={page * 20}")
  soup = BeautifulSoup(raw_html, 'html.parser')
  get_job_postings(soup, job_urls)

def clean_indeed_job_page(url): #  https://jessesw.com/Data-Science-Skills/
  raw_html = simple_get(url)
  soup = BeautifulSoup(raw_html, 'html.parser')

  for script in soup(["script", "style"]):
        script.extract() # Remove these two elements from the BS4 object
    
  page_text = soup.get_text() # Get the page_text from this   
  
  lines = (line.strip() for line in page_text.splitlines()) # break into lines 
 
  chunks = (phrase.strip() for line in lines for phrase in line.split("  ")) # break multi-headlines into a line each
  
  def chunk_space(chunk):
      chunk_out = chunk + ' ' # Need to fix spacing issue
      return chunk_out  
      
  page_text = ''.join(chunk_space(chunk) for chunk in chunks if chunk).encode('utf-8') # Get rid of all blank lines and ends of line
      
  # Now clean out all of the unicode junk (this line works great!!! 
  try:
      page_text = page_text.decode('unicode_escape') # Need this as some websites aren't formatted
  except:                                  # in a way that this works, can occasionally throw
      return                               # an exception
         
  page_text = re.sub("[^a-zA-Z.+3]"," ", page_text)  # Now get rid of any terms that aren't words (include 3 for d3.js)
                                           # Also include + for C++
  page_text = page_text.lower().split()  # Go to lower case and split them apart
          
  stop_words = set(stopwords.words("english")) # Filter out any stop words
  page_text = [w for w in page_text if not w in stop_words]
      
  page_text = list(set(page_text)) # Last, just get the set of these. Ignore counts (we are just looking at whether a term existed
                          # or not on the website)
  return page_text

def scrape_indeed_job_page(url):
  page_text = clean_indeed_job_page(url)
  print(page_text[:20])