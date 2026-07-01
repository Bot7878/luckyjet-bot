import requests
import re

URL = "https://1wpvkm.com/"

def get_results():
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        r = requests.get(URL, headers=headers, timeout=10)

        matches = re.findall(r"(\d+\.?\d*)x", r.text)
        results = [float(x) for x in matches]

        return results[-30:]

    except:
        return []
