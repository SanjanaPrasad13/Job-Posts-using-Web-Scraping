from bs4 import BeautifulSoup
import requests
import time

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=java&txtLocation=').text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')

def find_jobs():
    for index, job in enumerate(jobs):
            published_date = job.find('span', class_='sim-posted')
            #To show only recent job notifications
            if 'few' not in published_date.span.text:
                #Scraping the company name
                company_name = job.find('h3', class_ = 'joblist-comp-name').text
                #scraping the required skillset
                skill_set = job.find('span', class_ = 'srp-skills').text
                #job description link
                more_info = job.header.h2.a['href']
                #saving the information in different files
                with open(f'Scripts/post/{index}.txt', 'w') as f:
                    f.write(f'Company Name : {company_name.strip()}\n')
                    f.write(f'Skills Required : {skill_set.strip()}\n')
                    f.write(f'More Info : {more_info}\n')
                print(f'File Saved {index}')

    print("done")

if __name__ == '__main__':
    while True:
        find_jobs()
        #you can customize the repeating time for the program to execute
        time.sleep(6000) #for 60 minutes
