import time
from bs4 import BeautifulSoup
import requests 
import json 


headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.34"
}

def find_jobs():
    html_text = requests.get('https://www.gowork.pl/praca', headers=headers)
    src = html_text.text

    soup = BeautifulSoup(src, 'lxml')
    jobs = soup.find_all('div', class_ = 'job-item__content')
    for job in jobs:
        p_date = job.find('div', class_ = 'job-date')
        if 'dzisiaj' in p_date:
            c_name = job.find('a', class_ = 'g-company-name line-clamp-1')
            salary = job.find('div', class_ = 'g-job-salary')
            town2 = job.find('div', class_='g-job-location__title')
            town = job.find('div', class_='g-job-location--wrapper')
            with open(f'posts.txt', 'w') as f:
                f.write(f"Company name: {c_name.strip()}")
                f.write(f"Salary: {salary.strip()}")
    return jobs
    

        
if __name__ == "__main__":
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting {time_wait} seconds...')
        time.sleep(time_wait * 60)



# with open("all_categories_dict.json", "w") as file:
#     json.dump(src, file, indent=4, ensure_ascii=False)