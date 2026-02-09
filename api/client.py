import requests

class ApiClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()

    def post(self, endpoint, data=None, json=None):
        url = f"{self.base_url}{endpoint}"
        return self.session.post(url, data=data, json=json)
    
    def get(self, endpoint, params=None):
        url = f"{self.base_url}{endpoint}"
        return self.session.get(url, params=params)
