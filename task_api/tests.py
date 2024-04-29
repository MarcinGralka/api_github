import unittest
from unittest import mock
from unittest.mock import patch
from django.test import Client
import json

class SearchTestCase(unittest.TestCase):
    @patch('requests.get')
    def test_missing_keyword(self, mock_get):
        response = Client().get('/github/search/')
        assert response.status_code == 400
        assert response.json() == {'error': 'Keyword parameter is required'}

    @patch('requests.get')
    def test_successful_request(self, mock_get):
        mock_response = mock.Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'items': [
                {'name': 'test-repo', 'owner': {'login': 'test-user'},
                 'html_url': 'https://github.com/test-user/test-repo'},
            ]
        }
        mock_get.return_value = mock_response

        response = Client().get('/github/search/?keyword=test')
        assert response.status_code == 200
        data = json.loads(response.content)

        assert data['keyword'] == 'test'
        assert data['repositories'][0] == {'name': 'test-repo', 'owner_login': 'test-user',
                                           'url': 'https://github.com/test-user/test-repo'}
    