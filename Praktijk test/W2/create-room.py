import requests

access_token = "YmFkNjQ5NjctODIwMi00OWMxLThiODktMDFjYzNlMjVmZmFjMDMwYjQ0YWUtMzYy_PE93_f38a68ae-62d2-4efe-910e-b830048bb652"

url = "https://webexapis.com/v1/rooms"
headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}

data = {"title": "W2 Test Space - Djay"}
res = requests.post(url, headers=headers, json=data)

print(res.status_code)
print(res.json())
