from github_client import get_repository, search_repositories

##=======================================used to see if api calling is working=======================================
def extract_repository(owner, repo):

    data = get_repository(
        owner,
        repo
    )

    repository = {
        "name": data["name"],
        "owner": data["owner"]["login"],
        "language": data["language"],
        "stars": data["stargazers_count"],
        "forks": data["forks_count"],
        "created_at": data["created_at"],
        "updated_at": data["updated_at"]
    }

    return repository



def extract_repositories(query):
    data = search_repositories(query)

    repositories = []

    for repo in data["items"]:

        repository = {
            "id": repo["id"],
            "name": repo["name"],
            "full_name": repo["full_name"],
            "owner": repo["owner"]["login"],
            "language": repo["language"],

            "stars": repo["stargazers_count"],
            "forks": repo["forks_count"],
            "watchers": repo["watchers_count"],
            "open_issues": repo["open_issues_count"],
            
            "license": (
                repo["license"]["name"]
                if repo["license"]
                else None
            ),

            "created_at": repo["created_at"],
            "updated_at": repo["updated_at"],

            "url": repo["html_url"]
        }

        repositories.append(repository)

    return repositories