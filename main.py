from pyairtable import Api
from okta.client import Client as OktaClient

if __name__ == "__main__":
    api = Api("api-key-here")
    table = api.table("", "")
    print("here")
