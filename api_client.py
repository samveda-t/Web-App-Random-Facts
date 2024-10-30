import requests

def get_useless_fact():
    url = "https://uselessfacts.jsph.pl/api/v2/facts/random?language=en"
    response = requests.get(url, verify=False)  # Add verify=False
    if response.status_code == 200:
        data = response.json()
        return data['text']
    else:
        return "No fact available"
