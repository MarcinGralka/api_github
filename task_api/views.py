import json
import requests
from django.http import HttpResponse, JsonResponse

GITHUB_API_URL = 'https://api.github.com/search/repositories'


def search_repositories(request):
    keyword = request.GET.get('keyword')

    # Return error response if keyword is missing
    if not keyword:
        return JsonResponse({'error': 'Keyword parameter is required'}, status=400)

    # Replace with your actual GitHub API token for better rate limits and access control
    github_token = 'token'

    params = {
        'q': keyword
    }

    # Check if an API token is provided and make a request according to it
    if github_token == 'token' or github_token == '':
        response = requests.get(GITHUB_API_URL, params=params)
    else:
        headers = {
            'Authorization': f'token {github_token}'
        }
        response = requests.get(GITHUB_API_URL, params=params, headers=headers)

    # Check if the connection was successful
    if response.status_code == 200:
        data = response.json()
        repositories = []

        for repository in data.get('items', []):
            repositories.append(
                {
                    'name': repository['name'],
                    'owner_login': repository['owner']['login'],
                    'url': repository['html_url']
                }
            )

        # Prepare JSON data and return it as Http
        json_repositories = json.dumps({'keyword': keyword, 'repositories': repositories}, indent=4)

        return HttpResponse(json_repositories, content_type='application/json')
    else:
        # Return error response with details from the API call
        return JsonResponse({'error': 'Failed to retrieve data from Github API'}, status=response.status_code)
