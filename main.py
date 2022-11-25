import os

from boxsdk import Client, OAuth2
from dotenv import load_dotenv

load_dotenv()
auth = OAuth2(
    client_id=os.getenv('CLIENT_ID'),
    client_secret=os.getenv('CLIENT_SECRET'),
    access_token=os.getenv('ACCESS_TOKEN'),
)
client = Client(auth)

item_name = "test.txt"

items = client.folder(os.getenv('FOLDER_ID')).get_items()
for item in items:
    if item.name == item_name:
        item.delete()

folder_id = os.getenv('FOLDER_ID')
upload_file = client.folder(folder_id).upload("test.txt")
