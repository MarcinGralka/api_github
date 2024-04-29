import json
import unittest

import requests
from unittest.mock import patch
from django.test import Client
from .views import search_repositories

class SearchTestCase(unittest.TestCase):
    @patch('requests.get')
    def test_missing_keyword(self, mock_get):
        response = Client().get('/github/search/')
        assert response.status_code == 400
        assert response.json() == {'error': 'Keyword parameter is required'}

    