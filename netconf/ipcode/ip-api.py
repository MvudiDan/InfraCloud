import requests
from datetime import datetime
def get_ip_info():
    url = "https://api.myip.com"
    response = requests.get(url)
    now = datetime.now()
    formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
    print(f"🕒 Fetched at: {formatted_time}")
    if response.status_code == 200:
        data = response.json()
        print(f"🌍 Your IP Info:")
        print(f"IP Address: {data['ip']}")
        print(f"Country: {data['country']}")
        print(f"Country Code: {data['cc']}")
    else:
        print(f"❌ Failed to fetch IP info. Status code: {response.status_code}")
if __name__ == "__main__":
    get_ip_info()