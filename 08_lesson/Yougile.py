import requests

class Yougile:
    def __init__(self):
        self.BASE_URL = "https://ru.yougile.com/api-v2"
        self.company_id = "Ваш id"
        self.auth_token = None
        self.base_url = self.BASE_URL

    def get_auth_token(self):
        auth_url = f"{self.BASE_URL}/auth/keys/get"
        auth_data = {
    "login": "Ваш логин",
    "password": "Ваш пароль",
    "companyId": "ваш id"
}
        response = requests.post(auth_url, json=auth_data)
        if response.status_code == 200:
            data = response.json()
            self.auth_token = data[0].get("key")
            return response

    def create_project(self, title):
        if not self.auth_token:
            self.get_auth_token()
        url = f"{self.BASE_URL}/projects"
        headers = {
            "Authorization": f"Bearer {self.auth_token}",
            "Content-Type": "application/json"
        }
        json_data = {"title": title}
        response = requests.post(url, headers=headers, json=json_data)
        return response

    def update_project(self, project_id, new_title):
        if not self.auth_token:
            self.get_auth_token()
        url = f"{self.BASE_URL}/projects/{project_id}"
        headers = {
            "Authorization": f"Bearer {self.auth_token}",
            "Content-Type": "application/json"
        }
        json_data = {"title": new_title}
        response = requests.put(url, headers=headers, json=json_data)
        return response

    def get_project(self, project_id):
        if not self.auth_token:
            self.get_auth_token()
        url = f"{self.BASE_URL}/projects/{project_id}"
        headers = {"Authorization": f"Bearer {self.auth_token}"}
        response = requests.get(url, headers=headers)
        return response

    def get_projects(self):
        if not self.auth_token:
            self.get_auth_token()
        url = f"{self.BASE_URL}/projects"
        headers = {"Authorization": f"Bearer {self.auth_token}"}
        response = requests.get(url, headers=headers)
        return response


