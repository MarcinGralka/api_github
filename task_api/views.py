import json
import requests
from django.http import HttpResponse

GITHUB_API_URL = 'https://api.github.com/search/repositories'


def search_repositories(request):
    keyword = request.GET.get('keyword')

    response = requests.get(GITHUB_API_URL, params={'q': keyword})

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
