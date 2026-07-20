import os
from dotenv import load_dotenv
from pathlib import Path

#uncomment this line if testing locally only
#GITHUB_TOKEN = "PUT TOKEN HERE"

#since my python files ar in ingestion, and env file is in root, i need to provide that directory hence the .parent.parent which goes up 2 levels
env_path = Path(__file__).parent.parent / ".env"

#reads and excutes env file 
load_dotenv(env_path)


#fetch the environment variable (the github token entered by the user when running "docker run -e GITHUB_TOKEN=.... devpulse" ) and use that as the token for api calling. also works with env file BY READING the env variables inside 
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

#checking that there is a github token, if not then letting user know
if not GITHUB_TOKEN:
    raise ValueError(
        "Missing GITHUB_TOKEN. "
        "Set it as an environment variable or add it to your .env file."
    )

#same idea as github_token
AZURE_STORAGE_CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING")


if not AZURE_STORAGE_CONNECTION_STRING:
    raise ValueError(
        "Missing Azure storage connection string."
    )



BASE_URL = "https://api.github.com"


LANGUAGES = [
    "Python",
    "Java",
    "JavaScript",
    "TypeScript",
    "Go",
    "Rust",
    "Ruby",
    "C++",
    "C",
    "C#",
    "PHP",
    "Kotlin",
    "Swift",
    "Dart",
]