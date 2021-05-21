import requests

def client():
    # token_h = "Token 4f6924c1f17e7d1c0d7c4d9492699fa12dd7b86c"
    # headers = {"Authorization": token_h}
    # response = requests.get("http://localhost:8000/api/profiles/", headers=headers)
    credentials = {
        "username": "stefan",
        "email": "stefangouldson2019@gmail.com", 
        "password1": "changeme123",
        "password2": "changeme123"
        }
    response = requests.post("http://localhost:8000/dj-rest-auth/registration/", data=credentials)

    print("Status Code: ", response.status_code)
    response_data = response.json()
    print(response_data)

if __name__== "__main__":
    client()