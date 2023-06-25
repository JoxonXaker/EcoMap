import requests

url = "https://infobip.p.rapidapi.com/sms/1/reports"

headers = {
    "Authorization": "<REQUIRED>",
    "X-RapidAPI-Key": "5cd826cc48msh3767b3257e3e94dp191e55jsnf8db58313b6e",
    "X-RapidAPI-Host": "infobip.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.json())
