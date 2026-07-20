import requests
from config import GITHUB_TOKEN, BASE_URL

def get_headers():
    return{
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json"
    }

def get_repository(owner, repo):
    url = f"{BASE_URL}/repos/{owner}/{repo}"

    response = requests.get(
        url,
        headers=get_headers()
    )

    response.raise_for_status()

    return response.json()


def search_repositories(query, sort="stars", order="desc", per_page=100):
    url = f"{BASE_URL}/search/repositories"

    params = {
        "q": query,
        "sort": sort,
        "order": order,
        "per_page": per_page
    }

    response = requests.get(
        url,
        headers=get_headers(),
        params=params
    )

    response.raise_for_status()

    return response.json()