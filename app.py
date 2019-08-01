from scrape import scrape_indeed_feed
from scrape import scrape_indeed_job_page

NUM_PAGES_TO_SCRAPE = 2

def scrape_indeed(url):
  job_urls = []
  for i in range(0, NUM_PAGES_TO_SCRAPE):
    scrape_indeed_feed(url, i, job_urls)
  
  for job_url in job_urls:
    scrape_indeed_job_page(job_url)
  
# Indeed.ca "software engineering internship" - first page, filtered by internship, no location
scrape_indeed('https://www.indeed.ca/jobs?q=software+engineering+internship&jt=internship')
