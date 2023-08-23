import requests
from dataclasses import dataclass
from datetime import datetime
import time
file_path = r"C:/Users/shire/Downloads/le_chien.pptx"


@dataclass
class Status:
    """
        Represents the status and information about the processing of a file.
    """
    status: str
    filename: str
    timestamp: datetime
    explanation: str

class GPTExplainerClient:
    """
       A client class for interacting with the GPT Explainer web API.

    """
    def __init__(self, base_url):
        self.base_url = base_url

    def upload(self, file_path):

            files = [('file',open(file_path, 'rb')),('file',open(file_path, 'rb'))]
            response = requests.post(f"{self.base_url}/upload", files=files)
            response_json = response.json()
            if response.ok:
                return response_json['uid']
            else:
                raise Exception(response_json['error'])


    def status(self, uid):
            """
               Retrieves the processing status about a file.

               :param uid: The unique identifier (UID) of the file.
               :return: A `Status` object containing status information.
               :raises Exception: If the status request fails.
               """
            response = requests.get(f"{self.base_url}/status/{uid}")
            response_json = response.json()
            if response.ok:
                return Status(
                    status=response_json['status'],
                    filename=response_json['filename'],
                    timestamp=response_json['timestamp'],
                    explanation=response_json.get('explanation', None)
                )
            else:
                raise Exception(response_json['error'])


    @staticmethod
    def is_done(status_obj):
        return status_obj.status == 'done'


try:
    client = GPTExplainerClient("http://127.0.0.1:5001")
    uid = client.upload(file_path)
    print(f"UID: {uid}")
    time.sleep(60)
    status_obj = client.status(uid)
    if GPTExplainerClient.is_done(status_obj):
        print("File has been processed.")
    else:
        print("File is still pending processing.")
except Exception as e:
    print("Error:", e)