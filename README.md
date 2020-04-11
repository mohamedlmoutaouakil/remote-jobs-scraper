# RemoteJobsScraper
This project is a simple web scraper that scrapes stackoverflows's jobs section. It retrieve only remote job offers.

## Prerequisites 
To run the project you need to have [pipenv](https://pypi.org/project/pipenv/) installed, pipenv is tool that 
manages the python virtual envirenment and the dependencies of the project for you.

I have a windows OS, in my case I installed pipenv using the following command:
```bat
py -m install pipenv
```
## Running the main
main.py contains a script that takes from the terminal user typed keywords (job to look for) and prints a list of
python dictionaries representing the list of remote jobs found.

To run the script just run the main.py file in the root of the project:
```bat
python main.py
```
## Tests
The project has a one unit test, I used [pytest](https://docs.pytest.org/en/latest/) framework for unit tests.

To run unit tests use the following command:
```bat
py.test
```