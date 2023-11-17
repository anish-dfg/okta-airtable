import os

from dotenv import load_dotenv
from okta.client import Client as OktaClient
from pyairtable import Api


# NOTE: This is an example function that is being tested in test_main.py. Feel free to remove it once some real code is added  # noqa: E501
def add_ints(x: int, y: int) -> int:
    return x + y


if __name__ == "__main__":
    load_dotenv()
    api = Api(os.environ["AIRTABLE_ACCESS_TOKEN"])
    table = api.table(os.environ["AIRTABLE_BASE_ID"], os.environ["AIRTABLE_TABLE_ID"])
