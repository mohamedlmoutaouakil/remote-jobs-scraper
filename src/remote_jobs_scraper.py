import requests
from bs4 import BeautifulSoup

class RemoteJobsScraper:
    def __init__(self, URL):
        self.URL = URL

    def _get_results_list(self):
        html_page = requests.get(self.URL)
        # in case the response failure
        if not html_page.ok :
            return []
        soup = BeautifulSoup(html_page.content, 'html.parser')
        results = soup.find('div', class_='listResults')
        results_list = results.find_all('div', class_='-job')
        return results_list
    
    def get_jobs_list(self):
        results_list = self._get_results_list()
        jobs_list = []
        for job_post in results_list:
            job_title_elem = job_post.find('h2')
            company_name_header = job_post.find('h3')
            company_name_elem = company_name_header.find('span')
            location_elem = company_name_header.find_all('span')[-1]
            technologies_elements = job_post.find_all('a', class_=['post-tag', 'no-tag-menu'])
            if None in (job_title_elem, company_name_elem, technologies_elements):
                continue
            # Create and fill dictionary with job post info
            job_post_dict = {}
            job_post_dict['job_title'] = job_title_elem.text.strip()
            job_post_dict['company_name'] = company_name_elem.text.strip()
            job_post_dict['location'] = location_elem.text.strip()
            job_post_dict['technologies_list'] = [elem.text.strip() for elem in technologies_elements]
            jobs_list.append(job_post_dict)
        
        return jobs_list