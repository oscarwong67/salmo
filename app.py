from scrape import scrape_indeed_feed
from scrape import scrape_indeed_job_page
from collections import Counter

NUM_PAGES_TO_SCRAPE = 10

def scrape_indeed(url):
  job_urls = []
  for i in range(0, NUM_PAGES_TO_SCRAPE):
    scrape_indeed_feed(url, i, job_urls)
  
  job_words = []
  for job_url in job_urls:
    scrape_indeed_job_page(job_url, job_words)
  counts = Counter(job_words)
  print(counts.most_common(100))
  
# Indeed.ca "software engineering internship" - first page, filtered by internship, no location
# scrape_indeed('https://www.indeed.ca/jobs?q=software+engineering+internship&jt=internship')

# Indeed.com "software engineering internship" - first page, filtered by internship, no location
scrape_indeed('https://www.indeed.com/jobs?q=software%20engineering%20internship&jt=internship&vjk=a053bc5378958f13')
