import pytest
from unittest.mock import Mock, patch, MagicMock
from src.remote_jobs_scraper import RemoteJobsScraper
from tests.html_mock_response import test_response

@patch('src.remote_jobs_scraper.requests.get')
def test_get_jobs_list(mock_get):
    # ARRANGE
    # Configure requests.get() to return a mock object 
    # with statuts to OK and content as our html example
    mock_get.return_value.ok = True
    # Set content to html testing example contained in variable
    mock_get.return_value.content = test_response

    expected_job_dict = {}
    expected_job_dict['job_title'] = 'Senior Python Developer (Remote)'
    expected_job_dict['company_name'] = 'X-Team'
    expected_job_dict['location'] = 'No office location'
    expected_job_dict['technologies_list'] = ['python', 'django', 'flask']

    URL = 'test'
    remoteJobsScraper = RemoteJobsScraper(URL)

    # ACT
    actual_jobs_dicts = remoteJobsScraper.get_jobs_list()

    # ASSERT
    assert len(actual_jobs_dicts) == 1
    assert actual_jobs_dicts[0] == expected_job_dict