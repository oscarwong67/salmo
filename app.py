from scrape import scrape_indeed_feed
from scrape import scrape_indeed_job_page
from collections import Counter
import csv

NUM_PAGES_TO_SCRAPE = 9
OUTPUT_FILENAME = 'INDEED_USA_AUG_4_2019.csv'
langs = csv.DictReader(open("languages.csv")).fieldnames

def parse_skills(counts, parsed_skills):
  words_by_count = counts.most_common(300)
  for word_obj in words_by_count:
    if word_obj[0].lower() in langs:
      parsed_skills.append(word_obj)

def write_skills_csv(parsed_skills):
  with open(OUTPUT_FILENAME, 'wb') as out_file:
    writer = csv.writer(out_file)
    writer.writerow([b'language', b'num jobs'])
    for skill in parsed_skills:
      writer.writerow([skill[0].encode(), skill[1].encode()])

def scrape_indeed(url):
  job_urls = []
  for i in range(0, NUM_PAGES_TO_SCRAPE):
    scrape_indeed_feed(url, i, job_urls)
  
  job_words = []
  for job_url in job_urls:
    scrape_indeed_job_page(job_url, job_words)

  counts = Counter(job_words)

  parsed_skills = []
  parse_skills(counts, parsed_skills)
  write_skills_csv(parsed_skills)

def main():
  # Indeed.ca "software engineering internship" - first page, filtered by internship, no location
  # scrape_indeed('https://www.indeed.ca/jobs?q=software+engineering+internship&jt=internship')

  # Indeed.com "software engineering internship" - first page, filtered by internship, no location
  scrape_indeed('https://www.indeed.com/jobs?q=software%20engineering%20internship&jt=internship&vjk=a053bc5378958f13')
  
if __name__== "__main__":
  main()