import requests

access_token = "YmFkNjQ5NjctODIwMi00OWMxLThiODktMDFjYzNlMjVmZmFjMDMwYjQ0YWUtMzYy_PE93_f38a68ae-62d2-4efe-910e-b830048bb652"
room_id = "Y2lzY29zcGFyazovL3VybjpURUFNOmV1LWNlbnRyYWwtMV9rL1JPT00vM2U5ZWExMTAtZjg1NC0xMWYwLTgzZWUtNmIzNWY1NDdhNzYx"

url = f"https://webexapis.com/v1/rooms/{room_id}"
headers = {
    "Authorization": f"Bearer {access_token}"
}

res = requests.delete(url, headers=headers)

print(res.status_code)
if res.status_code == 204:
    print("Room deleted")
else:
    print(res.text)
