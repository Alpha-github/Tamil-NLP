import requests
import os
from urllib.parse import quote
import json



url = "https://google-translate1.p.rapidapi.com/language/translate/v2"
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"Accept-Encoding": "application/gzip",
	"X-RapidAPI-Key": os.getenv("X-RapidAPI-Key"),
	"X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
}

def english_tamil(text):
    s = quote(text)
    url_encoded_text = f"q={s}"
    payload = url_encoded_text+"&target=ta&source=en"

    response = requests.request("POST", url, data=payload, headers=headers)
    return response.text.encode('utf-8')

def tamil_english(text):
    s = quote(text)
    url_encoded_text = f"q={s}"
    payload = url_encoded_text+"&target=en&source=ta"

    response = requests.request("POST", url, data=payload, headers=headers)
    print("in")
    return(response.text['data'])

a = "நன்றி வருகிறேன்"
print(tamil_english(a))
