import json
from config import LANGUAGES
from github_client import get_repository, search_repositories
from extractor import extract_repository, extract_repositories
from uploader import upload_to_azure

#to show in terminal when running docker 
print("devpulse pipeline starting...")






##HELPER FUNCTION TO REMOVE DUPLICATES
def remove_duplicates(repositories):
    unique = {}

    for repo in repositories:
        unique[repo["id"]] = repo

    return list(unique.values())



##=======================================used to see if api calling is working=======================================
# repository = extract_repository(
#     "pytorch",
#     "pytorch"
# )

# with open(
#     "repository.json",
#     "w"
# ) as file:

#     json.dump(
#         repository,
#         file,
#         indent=4
#     )


# print("Data saved!")


####=======================================used to see if search_repos was working=======================================
# results = search_repositories(
#     query="language:Python stars:>1000"
# )

# print(results["total_count"])
# print(len(results["items"]))


##=======================================used to see if we can successfully retrieve a large number of repos for one language =======================================
# repositories = extract_repositories(
#     "language:Python stars:>1000"
# )

# print(f"Retrieved {len(repositories)} repositories.")

# with open(
#     "ingestion/output/repositories.json",
#     "w",
#     encoding="utf-8"
# ) as file:

#     json.dump(
#         repositories,
#         file,
#         indent=4,
#         ensure_ascii=False
#     )

# print("Repositories saved successfully!")



##now retrieve for multiple languages (top 100 repos from each)
all_repositories = []
for language in LANGUAGES:

    print(f"Collecting {language} repositories...")
    query = f"language:{language} stars:>1000"
    repositories = extract_repositories(query)
    all_repositories.extend(repositories)

##i want to see how many total repos did we find
print(f"\nCollected {len(all_repositories)} repositories.")

##now i am filtering them so i only store the unique ones IF there were duplicates
all_repositories = remove_duplicates(all_repositories)
print(f"Unique repositories: {len(all_repositories)}")

# #good to go save the output
with open(
    "ingestion/output/repositories.json",
    "w",
    encoding="utf-8"
) as file:

    json.dump(
        all_repositories,
        file,
        indent=4,
        ensure_ascii=False
    )

print("Repositories saved successfully!")

#uploading the json file to azure using the function made in uploader.py
upload_to_azure("ingestion/output/repositories.json","bronze/repositories.json")

#end of pipeline
print("pipeline complete")
