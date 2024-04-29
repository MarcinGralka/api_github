import json
import requests
from django.http import HttpResponse, JsonResponse

GITHUB_API_URL = 'https://api.github.com/search/repositories'


def search_repositories(request):
    keyword = request.GET.get('keyword')

    github_token = 'token'

    params = {
        'q': keyword
    }
    if github_token == 'token' or github_token == '':
        response = requests.get(GITHUB_API_URL, params=params)
    else:
        headers = {
            'Authorization': f'token {github_token}'
        }
        response = requests.get(GITHUB_API_URL, params=params, headers=headers)

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

        json_repositories = json.dumps({'keyword': keyword, 'repositories': repositories}, indent=4)

        return HttpResponse(json_repositories, content_type='application/json')
    else:
        return JsonResponse({'error': 'Failed to retrieve data from Github API'}, status=response.status_code)
