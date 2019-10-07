# salmo
salmo - Scraping Indeed.com/Indeed.ca to find the most popular software engineering internship skills.

Results are in "INDEED_USA_AUG_27_2019.csv", which contains a spreadsheet of the most-commonly mentioned programming languages on the first 10 pages of software engineering intern postings on Indeed.com

## How it works
The program queries Indeed.com and searches for software engineering internships, scraping it for job posting links, visiting each one and counting the number of times each word appears on the page. The words are then filtered out to only include programming languages, and outputted to a CSV file.

## Files
* app.py is the main file that calls different functions
* scrape.py handles parsing the content of Indeed.com
* query.py makes the HTTP requests
* languages.csv is a list of programming languages to reference
