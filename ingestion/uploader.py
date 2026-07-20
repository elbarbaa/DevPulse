from azure.storage.blob import BlobServiceClient

from config import AZURE_STORAGE_CONNECTION_STRING


CONTAINER_NAME = "github-data"


def upload_to_azure(file_path, blob_name):

    blob_service_client = BlobServiceClient.from_connection_string(AZURE_STORAGE_CONNECTION_STRING)

    blob_client = blob_service_client.get_blob_client(container=CONTAINER_NAME,blob=blob_name)

    with open(file_path, "rb") as data:
        blob_client.upload_blob(data,overwrite=True)

    print(f"Uploaded {blob_name} to Azure blob storage")