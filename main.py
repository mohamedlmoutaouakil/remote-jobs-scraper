from src.remote_jobs_scraper import RemoteJobsScraper
import pprint

def main():
    print('Welcome to remote jobs scraper!')
    search_input = input('Search for job : ')
    keywords = search_input.split(' ')
    # initialize URL
    URL = 'https://stackoverflow.com/jobs'
    if len(keywords) > 0 :
        q_parameter = '+'.join(keywords)
        URL = URL + '?q=' + q_parameter + '&r=true' # r=true to search for Remote jobs only
    # instanciate scraper class
    remoteJobsScraper = RemoteJobsScraper(URL)
    jobs_list = remoteJobsScraper.get_jobs_list()
    pp = pprint.PrettyPrinter()
    pp.pprint(jobs_list)

if __name__ == "__main__":
    main()