import requests

def client():
    token_h = "Token e88650b8cde7ea693b8612cc28300a6657ebedd5"
    # credentials = {"username": "sgouldson", "password": "password"}
    # response = requests.post("http://localhost:8000/dj-rest-auth/login/", data=credentials)

    headers = {"Authorization": token_h}

    response = requests.get("http://localhost:8000/api/profiles/", headers=headers)

    print("Status Code: ", response.status_code)
    response_data = response.json()
    print(response_data)

if __name__== "__main__":
    client()